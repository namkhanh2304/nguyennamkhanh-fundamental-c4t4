inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}
print("inventory:",inventory)
input("new item")
inventory["pocket"] =  ["seashell", "strange berry", "lint"]
print("inventory:",inventory)
input("you lost an item")
inventory ["backpack"].remove ("dagger")
print("inventory:",inventory)
input("it's your payday")
inventory["gold"] += 50
print("inventory:",inventory,)