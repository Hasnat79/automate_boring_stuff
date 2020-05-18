inventory={'arrow':12,"gold chain":42,
'rope':1,'torch':6,'dagger':1}
total=0
def displayInventory(inventory):
    global total
    for k,v in inventory.items():
        print("{} {}".format(v,k))
        total+=v
    print("Total number of items: {}".format(total))
displayInventory(inventory)
