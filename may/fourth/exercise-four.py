import traceback

def divide(x,y):
    try:
        return x/0
    except:
        traceback.print_exc()


def error_one(x,y):
    try:
        return divide(x,y)/0
    except:
        traceback.print_exc()


def main():
    try:
        print(error_one(3, 0)/0)
    except:
        traceback.print_exc()


if __name__ == '__main__':
    main()