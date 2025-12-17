from src.data_processing import add_numbers, multiply_numbers
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0


def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(0, 3) == 0

# print(test_add_numbers())
