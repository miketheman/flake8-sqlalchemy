from textwrap import dedent


def test_checker_unknown_call(helpers):
    """
    When the function call is not recognized, no error is raised from `Checker`.
    """
    sample_code = """
        class Model():
            _normalize_title = whatever()()
    """
    assert helpers.results(dedent(sample_code)) == set()
