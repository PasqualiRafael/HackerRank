def book_library(current, expection):    
    curr_day = current[0]
    curr_month = current[1]
    curr_year = current[2]
    
    exp_day = expection[0]
    exp_month = expection[1]
    exp_year = expection[2]

    fine = 0

    if curr_year > exp_year:
        fine = 10000
    elif curr_year == exp_year:
        if exp_month == curr_month and curr_day > exp_day:            
            fine = 15 * (curr_day - exp_day)
        elif curr_month > exp_month:            
            fine = 500 * (curr_month - exp_month)

    return fine

if __name__ == '__main__':        
    current = list(map(int, input().split(' ')))
    expection = list(map(int, input().split(' ')))
    print(book_library(current, expection))
    