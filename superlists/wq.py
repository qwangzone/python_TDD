class WTestM:
    def __enter__(self):
        print("进入 __enter__")
        return "WQ"
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("chuqv")


def show():
    return WTestM()


if __name__ == '__main__':
    with show() as s:
        print(s)
