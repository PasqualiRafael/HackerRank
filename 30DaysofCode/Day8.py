contact = int(input())    
book = list()
for i in range(contact):
    x, y = map(str, input().lstrip().rstrip().lower().split())
    phonebook = {'Name': x, 'Phone': y}
    book.append(phonebook)


for i in range(contact):        
    try:
        found = str(input())
        if found not in book[i]['Name']:
            print(f'Not found')
        else:                      
            print(f'{book[i]["Name"]}={book[i]["Phone"]}')
    except:
        break
               