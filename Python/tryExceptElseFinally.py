# try - except - else - finally 

while True:
    try:
        int_input = int(input("Give me some number : "))
    except:
        print("Plese try again, that was not a number!")
        continue
    else:
        print("Thanks... That was a number!")
        break
    finally:
        print("You see this line whatever happens...")

# END - Enes Cavus

