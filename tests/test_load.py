import pytest

from dundie.core import load

from .constants import PEOPLE_FILE


def setup_module():
    print()
    print("Roda antes dos testes desse módulo !\n")


def teardown_module():
    print()
    print("Roda depois dos testes desse módulo !\n")


@pytest.mark.unit
def test_load(request):
    """Test load function"""

    request.addfinalizer(lambda: print("Terminou"))

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == "J"
