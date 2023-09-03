import ast
from typing import Any, List, Optional

from ..issue import Issue


class Checker:
    @staticmethod
    def get_call_name(node: ast.Call) -> Optional[str]:
        if isinstance(node.func, ast.Attribute):
            return node.func.attr
        if isinstance(node.func, ast.Name):
            return node.func.id
        return None

    def run(self, node: Any) -> List[Issue]:  # TODO correct type hint
        raise NotImplementedError
