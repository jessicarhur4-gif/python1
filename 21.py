# 과제 #21: 높은 가격순으로 출력하기
price_input = input("물품 가격을 입력하세요 (세미콜론으로 구분): ")
price_list = list(map(int, price_input.split(";")))

price_list.sort(reverse=True)

for price in price_list:
    print(f"{price:>9}")