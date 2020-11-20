n = 12
l = []
for i in range(n):
    user = input().split()
    if user[0] == "insert":
        l.insert(int(user[1]), int(user[2]))       
    elif user[0] == "print":
        print(l)
    elif user[0] == "remove":
        l.remove(int(user[1]))
    elif user[0] == "append":
        l.append(int(user[1])))
    elif user[0] == "sort":
        l.sort()
    elif user[0] == "pop":
        l.pop()
    else:
        l.reverse()