#comment

def service_func():
    print("Hi, I'm sevice func that you call everywhere")
#comment1
def test_more(input: int):
    service_func()
    assert input > 2


#comment3
def main():
    test_more(3)
    print("ok")

if __name__ == "__main__":
    main()
