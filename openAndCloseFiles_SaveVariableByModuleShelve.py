baconFile = open('bacon.txt', 'w')
baconFile.write('Hello World!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
print content
# Hello World!
# Bacon is not a vegetable.



import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print shelfFile['cats']        # ['Zophie', 'Pooka', 'simon']
shelfFile.close()

shelfFile = shelve.open('mydata')
print list(shelfFile.keys())   # ['cats']
print list(shelfFile.values()) # [['Zophie', 'Pooka', 'simon']]
shelfFile.close()

