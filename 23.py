# 과제 #23: 숫자 리스트를 문자열로 변환하여 출력하기
user_input = input("숫자를 입력하세요 (공백으로 구분): ")
number_list = list(map(int, user_input.split()))

number_string = ", ".join(map(str, number_list))
print("문자열로 변환된 결과:", number_string)