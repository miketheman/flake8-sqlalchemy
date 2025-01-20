"""Checker for detecting `backref` usage in SQLAlchemy relationships."""

import ast

from ..issue import Issue
from ._base import Checker


class SQA300(Issue):
    code = "SQA300"
    message = f"{code} Use `back_populates` instead of `backref` in relationship"


class RelationshipBackrefChecker(Checker):
    def run(self, node: ast.Call) -> list[Issue]:
        """
        Checks if a relationship() call uses `backref` and suggests
        `back_populates` instead.
        """
        issues: list[Issue] = []

        if self.is_relationship_with_backref(node):
            issues.append(SQA300(node.lineno, node.col_offset))

        return issues

    @staticmethod
    def is_relationship_with_backref(node: ast.Call) -> bool:
        """
        Determines if the given node represents a relationship() call with a
        `backref` argument.
        """
        if RelationshipBackrefChecker.get_call_name(node) != "relationship":
            return False

        for keyword in node.keywords:
            if keyword.arg == "backref":
                return True

        return False
