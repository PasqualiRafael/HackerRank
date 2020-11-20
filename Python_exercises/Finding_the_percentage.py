n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    name = name.capitalize()    
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input().capitalize()



total = sum(student_marks[query_name])
media = float(total / 3)
print(student_marks[query_name])
print(f'{media:.2f}')