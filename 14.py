# 과제 #14: 숫자 5개를 입력받아 평균 구하기
user_input = input("숫자 5개를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

average = sum(number_list) / len(number_list)
print("평균:", average)