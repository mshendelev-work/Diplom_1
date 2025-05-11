import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert isinstance(buns[0], Bun)

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert isinstance(ingredients[0], Ingredient)
