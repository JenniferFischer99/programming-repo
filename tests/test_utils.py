from src.app.utils import sum_list, greet

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list(["4","5"]) == 9

def test_greet():
    assert greet("Alice") == "Hello, Alice!"


#SSBndWVzcyB5b3XigJl2ZSBmaWd1cmVkIG91dCBteSB5ZWFyLCBpZiBub3QsIGhlcmXigJlzIGEgbXkgbW9udGggaGludDogT2N0b2Jlcg==
