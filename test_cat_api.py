# test_cat_api.py

import pytest
from cat_api import get_random_cat_image_url


def test_get_random_cat_image_url_success(mocker):
    """
    Тестирует успешный запрос к TheCatAPI и проверяет, возвращает ли функция корректный URL.
    """
    # Мокаем ответ requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "id": "abc123",
            "url": "https://cdn2.thecatapi.com/images/abc123.jpg",
            "width": 800,
            "height": 600
        }
    ]

    mocker.patch('requests.get', return_value=mock_response)

    # Вызываем функцию
    result = get_random_cat_image_url()

    # Проверяем результат
    assert result == "https://cdn2.thecatapi.com/images/abc123.jpg"


def test_get_random_cat_image_url_failure(mocker):
    """
    Тестирует неуспешный запрос к TheCatAPI (например, статус код 404) и проверяет, возвращает ли функция None.
    """
    # Мокаем ответ requests.get с ошибочным статусом
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {}

    mocker.patch('requests.get', return_value=mock_response)

    # Вызываем функцию
    result = get_random_cat_image_url()

    # Проверяем результат
    assert result is None
