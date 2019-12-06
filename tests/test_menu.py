from app.database_module import Database
import pytest

@pytest.mark.usefixtures("setup_db")
class TestMenu:
    def test_initial_menu(self, setup_db):
        test_db = Database(setup_db)
        pass

    def test_menu_selection(self, setup_db):
        test_db = Database(setup_db)
        pass