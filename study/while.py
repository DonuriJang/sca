# treehit = 0
# while treehit < 10:
#      treehit = treehit + 1
#      print(f"나무를{treehit}번 찍었습니다.")
#      if treehit == 10:
#          print("나무 넘어갑니다.")

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

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print(f"남은 커피는{coffee}개 입니다.")
    if coffee == 0:
        print("커피가 없습니다.판매를 중지합니다")
        break

