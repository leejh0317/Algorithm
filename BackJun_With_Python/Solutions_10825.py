cnt = int(input())
student = [list(input().split()) for _ in range(cnt)]

student.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for val in student:
    print(val[0])