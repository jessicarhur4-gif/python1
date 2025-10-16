# 과제 #20: 숫자 5개를 입력받아 내림차순으로 정렬하기
user_input = input("숫자 5개를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

sorted_desc = sorted(number_list, reverse=True)
print("내림차순 정렬:", sorted_desc)