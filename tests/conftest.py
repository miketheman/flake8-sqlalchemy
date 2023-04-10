"""Testing configs, utilities, and fixtures for the tests package."""
import ast
from typing import Set

import pytest

from flake8_sqlalchemy import Plugin


class Helpers:
    @staticmethod
    def results(s: str) -> Set[str]:
        tree = ast.parse(s)
        plugin = Plugin(tree)
        return {f"{line}:{col + 1} {msg}" for line, col, msg, _ in plugin.run()}


@pytest.fixture
def helpers() -> Helpers:
    """Test helpers."""
    return Helpers
