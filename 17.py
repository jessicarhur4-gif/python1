# 과제 #17: 숫자 5개를 입력받아 10보다 큰 수만 출력하기
user_input = input("숫자 5개를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

filtered = [num for num in number_list if num > 10]
print("10보다 큰 수:", filtered)