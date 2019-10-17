import pytest

@pytest.mark.usefixtures("setup_db")
class TestLogin:
    def test_login_success(self, setup_db):
        pass

    def test_login_failure(self, setup_db):
        pass
