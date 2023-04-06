import argparse
from textwrap import dedent
import math as m
from functools import reduce

# ===============================================================================


def quiz_01():
    """
    변수 numbers 안에 있는 값들을 모두 로그 변환해주세요.
    로그 변환은 자연로그를 사용해주세요.

    math.log(x) : x의 자연로그를 반환합니다. (e를 밑으로 하는 로그)
    math.log(x, [base : int]) : x의 밑이 base인 로그를 반환합니다.
    """
    # Start my code here
    print(f"math.log(2) = {m.log(2)}")
    print(f"math.log(2, 2) = {m.log(2, 2)}")

    numbers = list(range(1, 11))
    print(f"numbers = {numbers}")
    print(f"log(numbers) = {list(map(m.log, numbers))}")
    print(f"log(numbers, 2) = {list(map(lambda x: m.log(x, 2), numbers))}")
    # End my code here
    return


# ===============================================================================


def quiz_02():
    """
    # 실습퀴즈2. 람다 표현식
    # 100 이하의 자연수 중에서 3의 배수가 아닌 숫자만 리스트에 담으세요.
    """

    # Start my code here
    filtered = list(filter(lambda x: x % 3 != 0, range(1, 101)))
    print(f"filtered = {filtered}")
    return


# ===============================================================================


def mul(x, y):
    return x * y


def quiz_03():
    """
    # 실습퀴즈3. 일급 객체
    # reduce 함수를 함께 사용하여 함수를 매개변수로 전달하는 코드를 작성해 보세요.
    """
    numbers = list(range(1, 11))
    print(f"numbers = {numbers}")
    # Start my code here
    print(f"reduce(mul, numbers) = {reduce(mul, numbers)}")
    print(
        f"reduce(lambda x, y: x * y, numbers) = {reduce(lambda x, y: x + y, numbers)}"
    )
    # End my code here
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
