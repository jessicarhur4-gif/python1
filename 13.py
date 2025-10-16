# 과제 #13: 숫자 5개를 입력받아 최댓값과 최솟값 출력하기
user_input = input("숫자 5개를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

max_value = max(number_list)
min_value = min(number_list)

print("최댓값:", max_value)
print("최솟값:", min_value)