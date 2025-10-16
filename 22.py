# 과제 #22: 숫자 여러 개를 입력받아 중복 제거 후 출력하기
user_input = input("숫자를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

unique_numbers = list(set(number_list))
print("중복 제거된 리스트:", unique_numbers)