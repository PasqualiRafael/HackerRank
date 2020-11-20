
def solve(day):
    people: int = 5
    share_ea_person: int = 3
    likes: int = 0    
    for ea_day in range(1, day+1):        
        likes += (people//2)
        people = (people//2) * share_ea_person
    return likes    
    


if __name__ == '__main__':
    day = int(input().strip())
    print(solve(day))