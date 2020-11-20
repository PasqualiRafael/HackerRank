def solve(min_students, arrival_time):
    arrival_time.sort()
    on_time = 0
    for x in arrival_time:
        if x <= 0:
            on_time += 1
    if on_time >= min_students:
        return f"NO"
    else:
        return f"YES"


if __name__ == "__main__":
    case_times = int(input())

    for _ in range(case_times):
        nk = input().split()
        num_students = int(nk[0])
        min_students = int(nk[1])

        arrival_time = list(map(int, input().rstrip().split()))

        print(solve(min_students, arrival_time))