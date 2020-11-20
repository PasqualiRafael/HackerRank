def solve(catA, catB, MouseC):
    catA = abs(MouseC - catA)
    catB = abs(MouseC - catB)
    if catA < catB:
        print('Cat A')
    elif catB < catA:
        print('Cat B')
    else:        
        print('Mouse C')

if __name__ == '__main__':
    times = int(input())

    for _ in range(times):
        xyz = input().split()            
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        solve(x, y, z)