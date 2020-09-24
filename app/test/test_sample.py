# pytest will run all files
# test_*.py or *_test.py
# current directory and its subdirectories

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5