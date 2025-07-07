import os
import json
import pytest
from src.utils import read_json


@pytest.fixture
def temp_json_file(tmpdir):
    data = {"test": "data", "value": 123}
    file_path = tmpdir.join("test.json")
    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(data, f)
    return str(file_path)


def test_read_json(temp_json_file):
    result = read_json(temp_json_file)
    assert result == {"test": "data", "value": 123}
    assert os.path.isabs(read_json(temp_json_file).get("_path", "")) is False


def test_read_json_nonexistent_file():
    """ Проверка поведения с несуществующим файлом"""
    non_existent_file = "non_existent_file.json"
    with pytest.raises(FileNotFoundError):
        read_json(non_existent_file)


def test_read_json_invalid_json(tmpdir):
    """Проверка с некорректным JSON"""
    invalid_json_file = tmpdir.join("invalid.json")
    invalid_json_file.write("{invalid json}")

    with pytest.raises(json.JSONDecodeError):
        read_json(str(invalid_json_file))

