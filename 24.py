# 과제 #24: 숫자 리스트를 역순으로 출력하기
user_input = input("숫자를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

reversed_list = list(reversed(number_list))
print("역순 리스트:", reversed_list)