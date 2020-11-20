def merge_the_tools(string, k):
    # your code goes here
    for i in range(len(string) // k):                       
        x = ''            
        for c in string[i * k: (i + 1) * k]:        
            if c in x:
                continue
            x += c
        print(x)

if __name__ == '__main__':
    string = 'AABCAAADA'
    k = 3
    merge_the_tools(string, k)

