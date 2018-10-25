# We expect output: 'apples, bananas, tofu, and cats'

spam = ['apples', 'bananas', 'tofu', 'cats']

def func(Parameter):
    Parameter[-1] = 'and '+ Parameter[-1]
    print "'"+ Parameter[0] + ', ' + Parameter[1] + ', ' + Parameter[2] + ', ' + Parameter[3] + "'"

func(spam)
# We expect output: ..00.00..
#                   .0000000.
#                   .0000000.
#                   ..00000..
#                   ...000...
#                   ....0....


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for j in range(6):
    for i in range(9):
        print grid[i][j],
    print '\n'