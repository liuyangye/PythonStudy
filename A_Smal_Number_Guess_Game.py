from random import randint
num = randint(1, 100)

print 'Guess what I think?'
bingo = False

while bingo == False:
    answer = input()

    if answer < num:
        print '%d is too small!' % answer
    if answer > num:
        print '%d is too big!' % answer
    if answer == num:
        print 'Bingo, %d is the right answer!' % answer
        bingo = True