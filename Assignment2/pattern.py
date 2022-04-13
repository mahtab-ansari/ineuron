'''for i in range(1,6):
    for x in range(1,(i+1)):
        print('*',end='')
    print('\n')
'''

def pattern(no_of_rows):
    for i in range(1,(no_of_rows+3)//2):
        for x in range(1,i+1):
            print('*', end='')
        print('\n')

    for y in range(i-1,0,-1):
        for z in range(1,y+1):
            print('*',end='')
        print('\n')

no_of_rows = int(input('Enter a Odd Number :'))
pattern(no_of_rows)
