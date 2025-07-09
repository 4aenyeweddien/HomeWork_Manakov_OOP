import json
import os
from typing import Any

from src.product import Product
from src.category import Category


def read_json(path: str) -> Any:
    """Читает Json файл и возвращает словарь"""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list[dict]) -> list:
    """Создает объекты из полученных данных Json файла"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
