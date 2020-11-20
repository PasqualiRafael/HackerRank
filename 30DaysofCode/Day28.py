def ask(q):
    box_email = list()
    valid_email = bool()
    _temp = list()
    for i in range(q):
        email = str(input())
        valid_email = findEmail(email)       
        if valid_email:
            _temp = email.split()
            box_email.append(_temp[0])
            box_email.sort()
    for x in box_email:            
        print(x)     
        
def findEmail(email):
    if email.find('@gmail.com') != -1:
        return True
    else:
        return False
        
if __name__ == '__main__':        
    q = int(input())    
    ask(q) 