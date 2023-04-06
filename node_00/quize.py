import argparse
from textwrap import dedent

# python 에서는 multi-line string을 작성할 때, """ 또는 '''를 사용한다.
# 이 때, """ 또는 '''를 사용하면, 문자열 내부에 작성된 줄바꿈 문자도 문자열에 포함된다.
# 이를 방지하기 위해, textwrap 모듈의 dedent 함수를 사용한다.
# dedent 함수는, 문자열의 indentation을 제거한다.

# ===============================================================================


def quiz_01():
    """
    실습퀴즈1. 복합 대입 연산자
    10을 4로 나눈 나머지 값이 c에 할당되도록 하는 복합 대입 연산자를 작성하세요.
    """
    c = 10
    # Start my code here
    c %= 4
    # End my code here
    print(c)  # 2가 출력 되어야 합니다.


# ===============================================================================


def quiz_02():
    """
    실습퀴즈2. 숫자형 연산과 복합 대입 연산자
    2의 8승을 d에 할당 되도록 하는 복합 대입 연산자를 작성하세요.
    """
    d = 2
    # Start my code here
    d **= 8
    # End my code here
    print(d)  # 256이 출력되어야 합니다.


# ===============================================================================


def quiz_03():
    """
    실습퀴즈3. 인덱싱
    인덱싱의 값이 ('o', '\t', 'p')으로 나올 수 있도록 문자열 c를 인덱싱해 보고, 그렇게 인덱싱한 이유를 작성해주세요.
    """
    c = "hello\tpython"
    # Start my code here
    # ret = (c[4], c[5], c[7])
    ret = tuple(c[4:7])
    # End my code here
    print(ret)  # ('o', '\t', 'p')가 출력되어야 합니다.

    print(
        dedent(
            """
        # 단순 인덱싱이라면 위와 같이 처리할 수 있다.
        # 문자열 자체는 iterable 하므로, tuple() 함수를 이용하여 tuple로 변환할 수 있다.
        # 이 때, 각각의 문자는 tuple의 원소가 된다.
        """
        )
    )


# ===============================================================================


def quiz_04():
    """
    실습퀴즈4. 뒤에서부터 인덱싱
    뒤에서부터 인덱싱을 하여 ('n', 'p', 'e')를 출력할 수 있는 코드를 작성해주세요.
    """

    c = "hello\tpython"
    # Start my code here
    # ret = (c[-1], c[-6], c[-12])
    ret = tuple(c[-1:-12:-5])
    # End my code here
    print(ret)  # ('n', 'p', 'e')가 출력되어야 합니다.


# ===============================================================================


def quiz_05():
    """
    실습퀴즈5. 리스트
    여러분이 좋아하는 음식이 담긴 리스트를 만들어보세요.
    """
    favorite_foods = ["pizza", "hamburger", "chicken"]
    print(f"내가 좋아하는 음식은 = {favorite_foods}")


# ===============================================================================


def quiz_06():
    """
    실습퀴즈6. 리스트의 인덱싱과 연산
    \'자란다자란다파이썬\'을 출력하고 싶다면, #q1~3에 각각 무엇이 들어갈까요? 이유도 함께 적어주세요.
    """

    quiz_list = ["잘잔다", "잘한다", "자란다", "잘할까", "화이팅", "힘내자"]
    python_list = ["파이썬", "PYTHON", "python"]

    answer = quiz_list[2] * 2 + python_list[0]
    print(answer)
    print(
        dedent(
            """
            # 코드 작성 이유: 리스트의 인덱싱과 연산을 이용하여, 자란다자란다파이썬을 출력하였다.
            # 문자열은 곱셈을 이용하면 반복해서 출력이 가능하며, 덧셈을 이용하면 문자열 concatenation이 가능하다.  
            """
        )
    )


# ===============================================================================


def quiz_07():
    """
    실습퀴즈7. 배타적 차집합
    A와 B가 겹치지않게 좋아하는 음식을 코드로 표현해주세요.
    """
    set_a = {"치킨", "민트초코", "파인애플피자"}
    set_b = {"치킨", "화이트초코", "페퍼로니피자"}
    # Start my code here
    answer = set_a ^ set_b
    # End my code here
    print(answer)  # {'민트초코', '파인애플피자', '화이트초코', '페퍼로니피자'}가 출력되어야 합니다.
    return


# ===============================================================================


def quiz_08():
    """
    실습퀴즈8. 딕셔너리
    아이펠의 몸무게 정보를 지워주세요.
    딕셔너리에서는 대괄호[] 안에 Key를 입력해야 삭제할 수 있어요.
    """
    quiz_dic = {"이름": "아이펠", "나이": 35, "MBTI": "ESFJ", "몸무게": 80}
    # Start my code here
    del quiz_dic["몸무게"]
    # End my code here
    print(quiz_dic)  # {'이름': '아이펠', '나이': 35, 'MBTI': 'ESFJ'}가 출력되어야 합니다.
    return


# ===============================================================================
def main(case_number: int) -> None:
    quiz_list = [quiz_01, quiz_02, quiz_03, quiz_04, quiz_05, quiz_06, quiz_07, quiz_08]
    if case_number == None:
        print("usage: quize_00.py [-h] [-c CASE_NUMBER]\nex) quize_00.py -c 1")
        return
    try:
        print(f"case_number: {case_number}")
        quiz_list[case_number - 1]()
        return
    except:
        print("case_number is out of range")
        return


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--case_number", type=int, help="case number")
    return parser.parse_args()


if __name__ == "__main__":
    main(get_arguments().case_number)
