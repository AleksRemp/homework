def fibonacci(how_many):
    a = 0
    b = 1
    for i in range(how_many):
        yield b
        a, b = b, a + b

if __name__ == '__main__':
    for i in fibonacci(10):
        print(i)