import ast
import importlib.metadata
from collections.abc import Generator
from typing import Any

from .checkers import (
    ColumnCommentChecker,
    ImportAliasChecker,
    RelationshipBackrefChecker,
)
from .issue import Issue


class Visitor(ast.NodeVisitor):
    checkers: dict[str, list[Any]] = {
        "Call": [
            ColumnCommentChecker(),
            RelationshipBackrefChecker(),
        ],
        "Import": [
            ImportAliasChecker(),
        ],
    }

    def __init__(self) -> None:
        self.issues: list[Issue] = []

    def capture_issues_from(self, visitor: str, node: ast.AST) -> None:
        for checker in self.checkers[visitor]:
            issues = checker.run(node)
            if issues:
                self.issues.extend(issues)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> Any:
        self.capture_issues_from("Call", node)

    def visit_Import(self, node: ast.Import) -> None:
        self.capture_issues_from("Import", node)


class Plugin:
    name = "flake8-sqlalchemy"
    version = importlib.metadata.version(name)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for issue in visitor.issues:
            yield issue.lineno, issue.col, issue.message, type(self)
