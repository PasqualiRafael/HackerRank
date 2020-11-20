

def split_and_join(line):
    # write your code here
    user_split = line.split()    
    user_join = '-'.join(user_split)    
    return user_join
    

texto = str('This is a string')
result = split_and_join(texto)
print(result)

