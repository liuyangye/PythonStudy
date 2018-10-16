'''if input 3, here are results we expected:
3
10
5
16
8
4
2
1
You finally get 1'''


def Collatz(number):
    if number % 2 == 0:
            return number / 2
    elif number % 2 == 1:
            return 3 * number + 1

print 'Whatever the integer you input, you will finally get 1. Please Enter an integer:\n'
value = Collatz(input())

while 1 != int(value):
    value = Collatz(int(value))
    print int(value)
    if 1 == int(value):
        print 'You finally get 1'
        break