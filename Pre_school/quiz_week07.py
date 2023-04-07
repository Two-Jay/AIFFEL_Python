import argparse
from textwrap import dedent
import random
import calc
import os

# ===============================================================================


def quiz_01():
    answer = [random.randint(1, 100) for _ in range(10)]
    print(f"answer = {answer}")
    return


# ===============================================================================


def quiz_02():
    print(calc.power(10, 5))
    print(calc.cubic(0.1))
    print(calc.divide(10, 7))
    print(calc.factorial(10))
    return


# ===============================================================================


def quiz_03():
    current_path = os.getcwd()
    print(f"path = {'/'.join([current_path, 'python.py'])}")
    return


# ===============================================================================
def main(case_number: int) -> None:
    quiz_list = [quiz_01, quiz_02, quiz_03]
    if case_number == None:
        print("usage: quize_00.py [-h] [-c CASE_NUMBER]\nex) quize_00.py -c 1")
        return
    try:
        print(f"case_number: {case_number}")
        quiz_list[case_number - 1]()
        return
    except IndexError:
        print(f"case_number is out of range.\nmaximum case_number is {len(quiz_list)}")
        return


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--case_number", type=int, help="case number")
    return parser.parse_args()


if __name__ == "__main__":
    main(get_arguments().case_number)
