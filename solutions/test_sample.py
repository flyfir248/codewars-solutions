import pytest
from solutions.reverse_string import solution  # Import your function

def test_reverse():
    assert solution("world") == "dlrow"
    assert solution("word") == "drow"
    assert solution("") == ""
    assert solution("a") == "a"
