import argparse
from textwrap import dedent

# ===============================================================================


def quiz_01():
    """
    # 실습퀴즈1. 리스트
    # list_tw에서 b를 출력해보세요.
    """
    list_tw = [[1, 2], ["ㄱ", "ㄴ"], ["a", "b"]]
    # Start my code here
    print(f"list_tw{list_tw}에서 '{list_tw[2][1]}'를 출력하려면, list_tw[2][1]을 입력하면 됩니다.")
    # End my code here
    return


# ===============================================================================


def quiz_02():
    """
    # 실습퀴즈2. 리스트
    # list_th에서 8과 h를 출력해보세요.
    """
    list_th = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
        [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]],
    ]

    print(f"8은 {list_th[0][2][1]}")
    print(f"h는 {list_th[1][2][1]}")
    return


# ===============================================================================


def quiz_03():
    """
    # 실습퀴즈3. 아스키 코드
    # AIFFEL의 아스키 코드를 알 수 있는 코드를 직접 작성해보세요.
    """
    original_str = "AIFFEL"
    # Start my code here
    ascii_str = ""
    for char in original_str:
        ascii_str += str(ord(char)) + " "
    print(ascii_str)
    # End my code here
    return


# ===============================================================================


def quiz_04():
    """
    # 실습퀴즈4. 컴프리헨션
    # 1부터 10까지의 숫자 중 홀수인 수를 모은 리스트를 만들어 보세요.
    """
    # Start my code here
    odd_list = []
    odd_list.append([i for i in range(1, 11) if i % 2 == 1])
    odd_list.append([i for i in range(1, 11, 2)])
    odd_list.append(list(range(1, 11, 2)))
    odd_list.append(list(filter(lambda x: x % 2 == 1, range(1, 11))))

    answer = [1, 3, 5, 7, 9]
    print(f"모두 {answer} 로 출력이 되었나요? : {all(answer == lst for lst in odd_list)}")
    # End my code here
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
