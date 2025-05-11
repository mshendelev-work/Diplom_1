import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    # Параметризация для тестирования различных типов ингредиентов
    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100, "SAUCE", "Hot Sauce", 100),
            (INGREDIENT_TYPE_FILLING, "Cutlet", 200, "FILLING", "Cutlet", 200),
        ]
    )
    def test_ingredient_initialization(self, ingredient_type, name, price, expected_type, expected_name, expected_price):
        # Создаем объект Ingredient
        ingredient = Ingredient(ingredient_type, name, price)

        # Проверяем, что атрибуты установлены корректно
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price
