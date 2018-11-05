
# Output:
#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(colWidths)):
        colWidths[i] = len(sorted(table[i], key = (lambda x: len(x)))[-1])
        print colWidths[i]

    for x in range(len(table[0])):
        for y in range(len(table)):
            print table[y][x].rjust(colWidths[y]),
        print ' '

printTable(tableData)

