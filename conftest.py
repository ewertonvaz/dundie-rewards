import pytest

MARKER = """
unit: Mark unit tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""


def pytest_configure(config):
    map(
        lambda line: config.addinivalue_line("markers", line),
        MARKER.split("\n"),
    )


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):  # injeção de dependências
    tmmpdir = request.getfixturevalue("tmpdir")
    with tmmpdir.as_cwd():
        yield

@pytest.fixture(autouse=True, scope="function")
def setup_testing_database(request):
    """For each test

    """