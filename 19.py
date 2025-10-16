# 과제 #19: 숫자 5개를 입력받아 첫 번째와 마지막 값 출력하기
user_input = input("숫자 5개를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

print("첫 번째 값:", number_list[0])
print("마지막 값:", number_list[-1])