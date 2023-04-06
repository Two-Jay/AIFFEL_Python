import argparse
from textwrap import dedent

# ===============================================================================

# 실습퀴즈1. 변수


def quiz_01():
    """
    # 실습퀴즈1. 변수
    # \'크리스마스는 12월 25일입니다.\' 라는 문장을 출력하고 싶습니다.
    """
    # Start my code here
    month = "12월"
    day = "25일"
    answer = f"{month} {day}"
    # End my code here
    print("크리스마스는", answer, "입니다🎄")
    return


# ===============================================================================


def quiz_02():
    """
    # 실습퀴즈2. 반복문
    # while문으로 구구단 13단을 만들어 보세요.
    """
    # Start my code here
    num = 1
    dan = 13
    while num <= dan:
        answer = dan * num
        print(f"{dan} * {num} = {answer}")
        num += 1
    # End my code here
    return


# ===============================================================================


def quiz_03():
    """
    # 실습퀴즈3. 비교 연산자
    # 기린(giraffe)은 원숭이(monkey)보다 키가 크다.
    # True가 나와야 정답입니다.
    """
    giraffe = 400
    monkey = 70

    # Start my code here
    print(f"기린은 원숭이보다 키가 큰가요? : {giraffe > monkey}")
    # End my code here
    return


# ===============================================================================


"귀엽다" and "착하다" and "빠르다"  # [[YOUR CODE]]

# 위의 코드를 풀어서 표현할 수도 있습니다.
# [[YOUR CODE]]


def quiz_04():
    """
    # 실습퀴즈4. 논리 연산자
    # 토끼는 귀엽고, 착하고, 빠르다.
    # True가 나와야 정답입니다.
    """
    rabbit = ["귀엽다", "착하다", "똑똑하다", "빠르다"]
    # Start my code here
    print(f"토끼는 귀엽고, 착하고, 빠른가? : { '귀엽다' and '착하다' and '빠르다' in rabbit }")
    # End my code here
    return


# ===============================================================================


def quiz_05():
    """
    # 실습퀴즈5. 기타 연산자
    # 로또 당첨 번호 7, 16, 25, 29, 35, 36, 28 중에 내가 고른 33번은 없다.
    # True가 나와야 정답입니다.
    """
    lotto_numbers = [7, 16, 25, 29, 35, 36, 28]
    my_number = [33]
    # Start my code here
    print(f"내가 고른 번호는 당첨 번호에 없는가? : {my_number not in lotto_numbers}")
    # End my code here
    return


# ===============================================================================


def quiz_06():
    """
    # 실습퀴즈6. 조건문
    # 앞으로 가면 강이고, 왼쪽으로 가면 산이다. 그 이외에는 막다른 절벽이다.
    """
    move = input("가고 싶은 곳을 넣어주세요. : ")
    # Start my code here
    if move == "front":
        print("강이 흐르고 있어.")
    elif move == "left":
        print("산이 있어.")
    else:
        print("막다른 절벽이야.")
    # End my code here
    return


# ===============================================================================


def my_profile(**kwargs):
    # Start my code here
    print("이름 : ", kwargs["name"])
    print("나이 : ", kwargs["age"])
    print("MBTI : ", kwargs["MBTI"])
    # End my code here
    return


# my_profile(# [[YOUR CODE]])
def quiz_07():
    """
    # 실습퀴즈7. 함수
    # 나만의 프로필 함수를 만들어 보세요.
    """
    # Start my code here
    me = {"name": "김정준", "age": 32, "MBTI": "ENFP"}
    my_profile(**me)
    # End my code here
    return


# ===============================================================================
def main(case_number: int) -> None:
    quiz_list = [quiz_01, quiz_02, quiz_03, quiz_04, quiz_05, quiz_06, quiz_07]
    if case_number == None:
        print("usage: quize_00.py [-h] [-c CASE_NUMBER]\nex) quize_00.py -c 1")
        return
    try:
        print(f"case_number: {case_number}")
        quiz_list[case_number - 1]()
        return
    except IndexError:
        print("case_number is out of range")
        return


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--case_number", type=int, help="case number")
    return parser.parse_args()


if __name__ == "__main__":
    main(get_arguments().case_number)
