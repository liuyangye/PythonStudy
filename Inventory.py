# Part 1 - Output:
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(list):
    print 'Inventory:'
    item_total = 0
    for k, v in list.items():
        print str(v) + ' ' + k
        item_total += v
    print 'Total number of items: ' + str(item_total)

displayInventory(stuff)


# Part 2 - Output:
# Inventory:
# 45 gold coin
# 1 rope
# 1 dagger
# 1 ruby
# Total number of items: 48

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
