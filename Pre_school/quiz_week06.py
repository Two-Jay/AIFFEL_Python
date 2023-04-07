import argparse
from textwrap import dedent
import sys

sys.tracebacklimit = 0

# ===============================================================================


def order_menu() -> list:
    menu = input("메뉴를 입력하세요: ")
    menu_count = input("메뉴의 개수를 입력하세요: ")
    return [menu, menu_count]


def quiz_01():
    order_result = order_menu()

    try:
        if order_result[0] != "햄버거":
            raise ValueError("햄버거만 주문 가능합니다.")
        menu_count = int(order_result[1])
    finally:
        print(f"주문하신 메뉴는 {order_result[0]}이고, {menu_count}개 입니다.")
    return


# ===============================================================================


def quiz_02() -> None:
    try:
        number = int(input("숫자를 입력하세요: "))
        print(f"입력하신 숫자는 {number}입니다.")
    except ValueError:
        print("ValueError : 숫자를 입력하세요.")
    else:
        print("예외가 발생하지 않았습니다.")
    finally:
        print("프로그램이 끝났습니다.")
    return


# ===============================================================================


def list_finder(lst: list, elt) -> int:
    try:
        idx = lst.index(elt)
        return idx
    except ValueError:
        return -1
    except Exception as e:
        print(f"Exception: {e}")


def quiz_03():
    print(list_finder([10, 9, 8], 8))
    print(list_finder([25, 7, 8], 10000))
    print(list_finder([100, 2, 15, 28, 0, "a-z가-하"], "a-z가-하"))
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
