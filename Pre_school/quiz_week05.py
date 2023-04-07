import argparse
from textwrap import dedent

# ===============================================================================


def hello():
    who = "아이펠"

    def hello2():
        nonlocal who
        who = "인유"

    hello2()
    print(f"hello {who}!")


def quiz_01():
    hello()
    return


# nonlocal 키워드를 이용해서 클로저 내부에서 외부의 변수를 변경할 수 있습니다.


# ===============================================================================


def intro(name):
    introduction = "My name is " + name + ". "

    def my(wish):
        nonlocal introduction
        introduction = introduction + "And I want to be a " + wish + ". "
        print(introduction)

    return my


def quiz_02():
    f = intro("인유")
    f("프로그래머")
    f("엔지니어")
    return


# nonlocal 키워드를 이용해서 클로저 내부에서 외부의 변수를 변경할 수 있습니다.
# 지금은 intro에서 클로저인 my를 리턴하고 있기 때문에, intro의 지역변수인 introduction을 참조할 수 있습니다.
# introduction은 intro의 특정 지역에 선언된 지역변수이지만, my에서도 클로저로써 참조할 수 있습니다.
# 따라서 introduction은 계속해서 매개변수로 전달되는 wish에 따라서 변경될 수 있습니다.
# 이처럼 함수 내부에서 함수를 리턴하는 경우, 내부 함수는 외부 함수의 지역변수를 참조할 수 있습니다.

# ===============================================================================


def closure_counter():
    count = 0

    def counter(num):
        nonlocal count
        count += num
        print(f"count: {count}")

    return counter


def quiz_03():
    counter = closure_counter()
    counter(20)
    counter(30)
    counter(40)
    counter(100)
    return


# ===============================================================================


def closure_str_checker():
    # 문자열이 길면 알려주는 함수
    def check_length(limit):
        def length_func(string):
            if len(string) > limit:
                return f"길이는 {len(string)}개 입니다. 지정한 길이보다 길어요."
            else:
                return "길이가 적당합니다."

        return length_func

    def str_checker(string):
        nonlocal check_length
        num_len = 20  # 길이를 설정합니다.
        length = check_length(num_len)
        if len(string) <= 0:
            print("문자열의 길이가 0보다 작거나 같습니다.")
        else:
            print(f"문자열의 길이 : {len(string)}, {length(string)}")

    return str_checker


def quiz_04():
    str_checker = closure_str_checker()
    str_checker("안녕하세요")
    str_checker("안녕하세요. 저는 인유입니다.")
    str_checker("")
    return


# ===============================================================================
def main(case_number: int) -> None:
    quiz_list = [quiz_01, quiz_02, quiz_03, quiz_04]
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
