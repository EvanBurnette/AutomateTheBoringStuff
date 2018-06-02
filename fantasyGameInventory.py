stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v

    print('Total number of items: ' + str(total))


def addToInventory(inventory, addedItems):
    for k in addedItems:
        inventory.setdefault(k, 0)
        inventory[k] += 1
    return inventory


stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
