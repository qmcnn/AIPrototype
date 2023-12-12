import argparse

def parse_input():
    parse = argparse.ArgumentParser()

    parse.add_argument(
        '--num',
        type = int,
        required = True,
        help='input for the multiplyby9 function'
    )
    args = parse.parse_input()
    return args

def printHello():
    print("Hello World!")

def multiplyby9(inputV):
    print(9*inputV)

if __name__ == "__main__":

    input_v = parse_input()

    print(f'the input num is {input_v.num}')
    print('we are in the main function')
    multiplyby9(20)
    printHello()
