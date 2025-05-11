import pytest
from praktikum.bun import Bun


class TestBun:
    # Параметризация для тестирования различных значений
    @pytest.mark.parametrize(
        "name, price, expected_name, expected_price",
        [
            ("Black Bun", 100, "Black Bun", 100),
            ("White Bun", 200, "White Bun", 200),
            ("Red Bun", 300, "Red Bun", 300),
        ]
    )
    def test_bun_initialization(self, name, price, expected_name, expected_price):
        # Создаем объект Bun
        bun = Bun(name, price)

        # Проверяем, что атрибуты установлены корректно
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price
