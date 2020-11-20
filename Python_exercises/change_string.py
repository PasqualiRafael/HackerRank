def mutate_string(string, position, character):
    l = list(string)
    if position > len(string):
        l.append(character)
    else:        
        l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input(f'Type any word.\n')
    i, c = input(f'Type one number and one letter separete by space.\n').split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
