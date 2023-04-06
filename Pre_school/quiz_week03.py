import argparse
from textwrap import dedent
import sys
from functools import wraps

# ===============================================================================


def quiz_01():
    """
    실습퀴즈 1. 리스트와 제너레이터의 메모리 사이즈 비교하기
    제너레이터 표현식을 활용해서 #[[YOUR CODE]] 부분을 완성하여 리스트와 제너레이터의 메모리 사이즈를 비교해보세요.
    리스트와 제너레이터의 메모리 사이즈가 다른 이유는 무엇인지 적어보세요.
    """
    sample_list = [i for i in range(1000000)]
    sample_generator = (i for i in range(1000000))

    print(f"list size: {sys.getsizeof(sample_list)}")
    print(f"generator size: {sys.getsizeof(sample_generator)}")

    print(
        dedent(
            """
        # 리스트와 제너레이터의 메모리 사이즈가 다른 이유는 무엇인가요?
        # 리스트는 모든 값을 메모리에 저장하고, 제너레이터는 값을 하나씩 생성합니다.
        """
        )
    )
    return


# ===============================================================================

# 위의 제너레이터식은 함수로도 구현이 가능합니다.


def gen(min=0, max=0, step=1, condition=lambda x: True):
    for i in range(min, max, step):
        if condition(i):
            yield i


# ===============================================================================


class ThisisDecorator:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print("🐠🐟🐡🐬🦈🦭🐳🐋🐙🦑🦞🦀🦐")
        self.func()
        print("🐆🐅🐃🐂🐄🦬🐪🐫🦙🐘🦏🦛🦣")


class Peace:
    @ThisisDecorator
    def peace_function():
        print("peace")


def quiz_02():
    peace = Peace()
    peace.peace_function()
    return


# ===============================================================================

# 물론 위의 문제도 함수로 구현이 가능합니다.


def ThisisDecoratorfunc(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("🐠🐟🐡🐬🦈🦭🐳🐋🐙🦑🦞🦀🦐")
        f(*args, **kwargs)
        print("🐆🐅🐃🐂🐄🦬🐪🐫🦙🐘🦏🦛🦣")

    return wrapper


class Peace:
    @ThisisDecoratorfunc
    def peace_function(self):
        print("peace")


def quiz_02_ex():
    peace = Peace()
    peace.peace_function()
    return


# ===============================================================================
def main(case_number: int) -> None:
    quiz_list = [quiz_01, quiz_02, quiz_02_ex]
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
