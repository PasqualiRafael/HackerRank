

def f_cap(s):
    c = 0
    user_cap = list()

    user_split = s.split()
    
    for x in user_split:        
        user_cap.append(user_split[c].capitalize())
        c += 1

    user_join = " ".join(user_cap)
    
    
    
    return user_join



s = input(f'Qual seu nome?\n')
# s = 'rafael pasquali'

result = f_cap(s)

print(result + '\n')


# def f_cap(s):
#     x = s.split(' ')
#     for i in range(len(x)):
#         x[i] = x[i].capitalize()        
#     return ' '.join(x)

#     # return x.title()


# s = '1 w 2 r 3g'
# print f_cap(s))