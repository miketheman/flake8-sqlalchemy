import ast
from typing import Any, List

from ..issue import Issue


class Checker:
    @staticmethod
    def get_call_name(node: ast.Call) -> str:
        if isinstance(node.func, ast.Attribute):
            return node.func.attr
        if isinstance(node.func, ast.Name):
            return node.func.id
        # Fallthrough for any unknown conditions. Eventually remove this.
        raise Exception(f"Unknown node.func type for {node.func}")  # pragma: no cover

    def run(self, node: Any) -> List[Issue]:  # TODO correct type hint
        raise NotImplementedError
