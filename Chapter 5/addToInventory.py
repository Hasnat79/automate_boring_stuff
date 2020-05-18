def addToInventory(inventory, addedItems):
    
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i]=inventory[i]+1
    return inventory
def displayInventory(inventory):
    total =0
    for k,v in inventory.items():
        print("{} {}".format(v,k))
        total+=v
    print("Total number of items: {}".format(total))
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)