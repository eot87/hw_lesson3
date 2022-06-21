
def service_func():
    print("Hi, I'm sevice func that you call everywhere")

def test_more(input: int):
    service_func()
    assert input > 2

def test_less(input: int):
    service_func()
    assert input < 2

def main():
    test_less(3)
    test_more(3)
