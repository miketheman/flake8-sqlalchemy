import pytest

from flake8_sqlalchemy import Plugin
from flake8_sqlalchemy.checkers._base import Checker


def test_plugin_version():
    assert isinstance(Plugin.version, str)
    assert "." in Plugin.version


def test_plugin_name():
    assert isinstance(Plugin.name, str)


def test_trivial_case(helpers):
    assert helpers.results("") == set()


def test_base_checker_raises_not_implemented_error():
    with pytest.raises(NotImplementedError):
        Checker().run("")
