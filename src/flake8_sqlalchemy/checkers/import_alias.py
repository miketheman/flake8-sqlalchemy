"""Checks that the sqlalchemy import is aliased as `sa` or `db`."""

import ast

from ..issue import Issue
from ._base import Checker


class SQA100(Issue):
    code = "SQA100"
    message = f"{code} Import alias sqlalchemy as `sa` or `db`"


class ImportAliasChecker(Checker):
    def run(self, node: ast.Import) -> list[Issue]:
        """
        Checks if the `sqlalchemy` module is imported with an alias
        other than `sa` or `db`.
        """
        issues: list[Issue] = []

        for alias in node.names:
            if alias.name == "sqlalchemy" and alias.asname not in (None, "sa", "db"):
                issues.append(SQA100(node.lineno, node.col_offset))

        return issues
