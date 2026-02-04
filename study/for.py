# test_list = ['one','two','three' ]
# for i in test_list:
#     print(i)

# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first + last)

# marks1.py 60점이 이상이면 합격하는 프로그램
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print(f'{number}번 학생은 합격입니다.')
#     else:
#         print(f'{number}번 학생은 불합격입니다.')

# marks2.py 60점 이상이면 축하 메세지 보내는 프로그램
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark < 60: continue
#     print(f'{number}번 학생 합격입니다. 축하합니다')

# add = 0
# for i in range(1,11):
#     add = add + i
# print(add)

#marks3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print(f'{number+1}번 학생 축하합니다. 합격입니다.')
