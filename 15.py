# 과제 #15: 숫자 5개를 입력받아 오름차순으로 정렬하기
user_input = input("숫자 5개를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

sorted_list = sorted(number_list)
print("오름차순 정렬:", sorted_list)