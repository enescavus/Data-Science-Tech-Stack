# map filter quick practices 
names = ["enes", "arzu", "ali", "faruk"]
def mapFilterFunction(name):
    if "a" in name:
        return True
    else:
        return False
print("Map function output : " , list(map(mapFilterFunction, names)))
print("Filter function output : " , list(filter(mapFilterFunction, names)))
# END - Enes Cavus