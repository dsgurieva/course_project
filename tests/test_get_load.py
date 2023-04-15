from utils import get_load
def test_get_load():
    test_data = [
      {
        "one": 1,
        "two": 2,
        "tree": 3
      }
    ]

    assert test_data == get_load("tests/test_operation.json")
