import pytest


# scope="session" makes it shared between tests
@pytest.fixture(scope="session")
def minimal():
    # defining something to pass thourh tests
    pass
