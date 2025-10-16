# 과제 #11: 숫자 5개 입력받아 리스트로 변환
user_input = input("숫자 5개를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))
print("리스트:", number_list)