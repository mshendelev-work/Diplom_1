import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:
    # Моки для тестирования взаимодействия с другими классами
    @pytest.fixture
    def mock_bun(self):
        mock = Mock(spec=Bun)
        mock.get_name.return_value = "Mock Bun"
        mock.get_price.return_value = 50
        return mock

    @pytest.fixture
    def mock_ingredient(self):
        mock = Mock(spec=Ingredient)
        mock.get_name.return_value = "Mock Ingredient"
        mock.get_type.return_value = "SAUCE"
        mock.get_price.return_value = 10
        return mock

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 0)
        assert burger.ingredients[0] == mock_ingredient

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price()

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert "(==== Mock Bun ====)" in receipt
        assert "= sauce Mock Ingredient =" in receipt
        assert "Price:" in receipt
