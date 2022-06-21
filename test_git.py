#comment
#comment1

def service_func():
    print("Hi, I'm sevice func that you call everywhere")

#comment2
def test_more(input: int):
    service_func()
    assert input > 2

def test_less(input: int):
    service_func()
    assert input < 2

def main():
    test_less(1)
    test_more(3)
    print("ok")

if __name__ == "__main__":
    main()
