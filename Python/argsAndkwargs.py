# args and kwargs practices 


# returns tuple *args
def returnMaxArgs(*args):
    return max(args)

def returnSumArgs(*args):
    return sum(args)

print("Max funciton - data given 5,10,15,20 : " , returnMaxArgs(5,10,15,20))
print("Sum funciton - data given 5,10,15,20 : " , returnSumArgs(5,10,15,20))

# returns dict **kwargs
def checkMyName(**kwargs):
    if "Enes" in kwargs:
        return ("Name Found")
    else:
        return ("Name Not Found")

print("KWARGS function - : " , checkMyName(Enes = 11, SomeOneElse = 10))

# END - Enes Cavus
