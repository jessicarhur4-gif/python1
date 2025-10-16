# 과제 #12: 숫자 5개를 입력받아 짝수만 출력하기
user_input = input("숫자 5개를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

even_numbers = [num for num in number_list if num % 2 == 0]
print("짝수만 출력:", even_numbers)