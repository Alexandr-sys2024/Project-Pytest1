# cat_api.py

import requests
from typing import Optional


def get_random_cat_image_url() -> Optional[str]:
    """
    Делает запрос к TheCatAPI для получения случайного изображения кошки.

    Returns:
        str: URL изображения кошки, если запрос успешен и данные корректны.
        None: В противном случае.
    """
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url, timeout=5)  # Добавлен таймаут для предотвращения зависания
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0 and 'url' in data[0]:
                return data[0]['url']
        # В случае любого другого статуса или некорректных данных
        return None
    except requests.RequestException as e:
        # Логирование ошибки можно добавить здесь, если необходимо
        return None
