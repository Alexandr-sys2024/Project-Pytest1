# example_usage.py

from cat_api import get_random_cat_image_url

def main():
    url = get_random_cat_image_url()
    if url:
        print(f"Случайное изображение кошки: {url}")
    else:
        print("Не удалось получить изображение кошки.")

if __name__ == "__main__":
    main()
