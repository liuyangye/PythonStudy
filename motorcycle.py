motorcycles = ['honda', 'yamaha', 'suzuki']
print motorcycles

motorcycles[0] = 'ducati'
print motorcycles

motorcycles.append('ducati')
print motorcycles

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print motorcycles
del motorcycles[1]
print motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki']
print motorcycles
popped_motorcycle = motorcycles.pop()
print motorcycles
print popped_motorcycle

motorcycles = ['honda', 'yamaha', 'suzuki']
last_ownd = motorcycles.pop()
print 'The last motorcycle I owned was a ' + last_ownd.title() + '.'
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print 'The first motorcycle I owned was a ' + first_owned.title() + '.'

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print motorcycles
print ('\nA ' + too_expensive.title() + 'is too expensive for me.')