# 과제 #18: 숫자 5개를 입력받아 합계 구하기
user_input = input("숫자 5개를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

total = sum(number_list)
print("합계:", total)