import argparse
from textwrap import dedent
import random
import calc
import os

# ===============================================================================


class Shoes:
    production_count = 0

    def __init__(self, size, color, brand):
        self.size = size
        self.color = color
        self.brand = brand
        Shoes.production_count += 1
        self.shoes_count()
        print(f"{self.size}, {self.color}, {self.brand}인 신발은 만들었습니다.")

    def __str__(self):
        return f"size: {self.size}, color: {self.color}, brand: {self.brand}"

    def color_change(self, color):
        self.color = color

    def shoes_count(self):
        print(f"생산된 신발의 수: {Shoes.production_count}")
        return Shoes.production_count


def quiz_01():
    shoes_01 = Shoes(250, "black", "nike")
    shoes_02 = Shoes(270, "white", "adidas")
    shoes_03 = Shoes(240, "red", "puma")

    print(shoes_01)
    print(shoes_02)
    print(shoes_03)
    return


# ===============================================================================


def quiz_02():
    shoes_01 = Shoes(250, "black", "nike")
    shoes_02 = Shoes(270, "white", "adidas")

    shoes_01.color_change("red")
    shoes_02.color_change("red")

    print(shoes_01)
    print(shoes_02)
    return


# ===============================================================================


# 실습퀴즈4. 클래스 3  
# 모두의연구소를 소개하는 클래스를 만들어 보세요.

class Modulabs:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def describe(self):
        return f"{self.name}은 {self.value}."

class FlippedSchool(Modulabs): 
    def __init__(self, name, value):
        super().__init__(name, value)

    def describe(self):
        return f"{super().describe()}"

class Aiffel(Modulabs): 
    def __init__(self, name, value):
        super().__init__(name, value)

    def describe(self):
        return f"{super().describe()}"

class Lab(Modulabs): 
    def __init__(self, name, value):
        super().__init__(name, value)

    def describe(self):
        return f"{super().describe()}"

class Modu:
    def __init__(self, name, modulabs):
        self.name = name
        self.modulabs = modulabs

    def describe(self):
        modulabs_descriptions = [modulab.describe() for modulab in self.modulabs]
        return f"{self.name}에는 다음과 같은 프로그램들이 있습니다 :\n" + "\n".join(modulabs_descriptions)

def quiz_03():
    modulabs1 = Modulabs("모두연", "지식을 공유하며 경험을 통해 배우는 열린 연구소")
    modulabs2 = FlippedSchool("풀잎스쿨", "함께 성장하는 플립 러닝 기반 스터디 모임")
    modulabs3 = Aiffel("아이펠", "함께 탐험하며 성장하는 AI 학교")
    modulabs4 = Lab("LAB","연구하며 논문도 쓸 수 있는 연구 모임")

    modu = Modu("모두연", [modulabs1, modulabs2, modulabs3, modulabs4])
    print(modu.describe())
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
