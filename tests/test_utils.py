# import json
# import pytest
# from pathlib import Path
# from src.main import Category, Product
# from src.utils import read_json, create_objects_from_json
#
#
# @pytest.fixture
# def sample_json_data():
#     return [{
#         "name": "Test Category",
#         "description": "Test Description",
#         "products": [{
#             "name": "Test Product",
#             "description": "Product Desc",
#             "price": 100.0,
#             "quantity": 5
#         }]
#     }]
#
#
# def test_read_json_valid_file(tmp_path):
#     """Тест чтения корректного JSON-файла"""
#     test_data = {"test": "data"}
#     file_path = tmp_path / "test.json"
#     file_path.write_text(json.dumps(test_data))
#
#     result = read_json(file_path)
#     assert result == test_data
#     assert isinstance(result, dict)
#
#
# def test_read_json_nonexistent_file():
#     """Тест обработки отсутствующего файла"""
#     with pytest.raises(FileNotFoundError):
#         read_json("nonexistent.json")
#
#
# def test_create_objects_valid_data(sample_json_data):
#     """Тест создания объектов из валидных данных"""
#     categories = create_objects_from_json(sample_json_data)
#
#     assert len(categories) == 1
#     category = categories[0]
#
#     # Проверка категории
#     assert isinstance(category, Category)
#     assert category.name == "Test Category"
#     assert category.description == "Test Description"
#
#     # Проверка продукта
#     assert len(category.products) == 1
#     product = category.products[0]
#     assert isinstance(product, Product)
#     assert product.name == "Test Product"
#     assert product.price == 100.0
#     assert product.quantity == 5
#
#
# def test_create_objects_empty_data():
#     """Тест обработки пустого списка данных"""
#     result = create_objects_from_json([])
#     assert result == []
#
#
# def test_create_objects_missing_fields(sample_json_data):
#     """Тест обработки данных с отсутствующими обязательными полями"""
#     # Удаляем обязательное поле
#     del sample_json_data[0]["products"][0]["quantity"]
#
#     with pytest.raises((TypeError, KeyError)):
#         create_objects_from_json(sample_json_data)
#
#
# def test_full_integration(tmp_path, sample_json_data):
#     """Тест полного цикла: запись -> чтение -> создание объектов"""
#     # 1. Запись тестовых данных
#     test_file = tmp_path / "integration_test.json"
#     test_file.write_text(json.dumps(sample_json_data))
#
#     # 2. Чтение файла
#     data = read_json(test_file)
#     assert data == sample_json_data
#
#     # 3. Создание объектов
#     categories = create_objects_from_json(data)
#
#     # 4. Проверка результатов
#     assert len(categories) == 1
#     category = categories[0]
#     assert isinstance(category, Category)
#
#     product = category.products[0]
#     assert product.quantity == 5
#     assert product.price == 100.0