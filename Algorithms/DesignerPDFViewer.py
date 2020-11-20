def solve(h, word):

    alphabetic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
     
    words_list = []
    
    for chars in word:
       words_list.append(chars)

    words_length = len(words_list)

    words_list = list(set(words_list))    
    words_list.sort()
    
    words_dict = dict(zip(alphabetic, h))   
   
    letter_high = max(words_dict[x] for x in words_list)    
    result = letter_high * words_length

    return result    
 
 
if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = str(input())
    print(solve(h, word))
