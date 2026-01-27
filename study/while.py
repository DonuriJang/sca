# treehit = 0
# while treehit < 10:
#      treehit = treehit + 1
#      print(f"나무를{treehit}번 찍었습니다.")
#      if treehit == 10:
#          print("나무 넘어갑니다.")
from operator import truediv

# prompt ="""
# 1. Add
# 2. Del
# 3. List
# 4. Quit
#
# Enter number: """
# number = 0
# while number !=4:
#     print(prompt)
#     number = int(input())

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee - 1
#     print(f"남은 커피는{coffee}개 입니다.")
#     if coffee == 0:
#         print("커피가 없습니다.판매를 중지합니다")
#         break

coffee = 10
money = 300
while True:
    money = int(input("돈을 넣어주세요:"))
    if money > 300:
        coffee = coffee - 1
        print(f"거스름돈{money-300}원을 주고 커피를 줍니다.")
        print(f"남은 커피의 개수는 {coffee}개 입니다.")
    elif money == 300:
        coffee = coffee -1
        print("커피를 줍니다.")
        print(f"남은 커피의 개수는 {coffee}개 입니다.")
    else:
        print("커피를 안줍니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break


