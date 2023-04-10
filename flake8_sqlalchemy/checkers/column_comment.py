"""Checks that Columns have comments."""

import ast
from typing import List

from ..issue import Issue
from ._base import Checker


class SQA200(Issue):
    code = "SQA200"
    message = f"{code} Column missing comment keyword argument"


class ColumnCommentChecker(Checker):
    def run(self, node: ast.Call) -> List[Issue]:
        """
        Checks if a `sqlalchemy.Column` is missing a `comment` keyword argument.
        """
        issues: List[Issue] = []

        if self.is_column(node) and not self.has_comment(node):
            issues.append(SQA200(node.lineno, node.col_offset))

        return issues

    def is_column(self, node: ast.Call) -> bool:
        call_name = self.get_call_name(node)
        if call_name == "Column":
            return True
        return False

    def has_comment(self, node: ast.Call) -> bool:
        return self.has_keyword(node, "comment")

    def has_keyword(self, node: ast.Call, keyword: str) -> bool:
        for keyword_node in node.keywords:
            if keyword_node.arg == keyword:
                return True
        return False
