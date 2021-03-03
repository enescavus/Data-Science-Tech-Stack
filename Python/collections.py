"""
author : Enes Çavuş
subject : hackerrank solutions - collections
date : 2 March 2021
goal : understanding 'collections'

"""

# NOTE: this code specified for hackerrank input. Needs a specific input.

################################### Counter() function


from collections import Counter

if __name__ == '__main__':
    n = map(int, input().split())
    shoes = dict(Counter(map(int,input().split())))
    customer_count = int(input())
    gelir = 0
    
    for i in range(customer_count):
        order = list(map(int, input().split()))
        if order[0] in shoes.keys() and shoes[order[0]] > 0:
            gelir += int(order[1])
            shoes[order[0]] = shoes[order[0]] - 1

    print(gelir)


################################### deque() function
# NOTE: this is an another python code. This one is here bacause it is about Collections !
# Run as a seperate python file, also this one needs a specific input. 
# Check hackerrank python challenges! for more ...

from collections import deque

if __name__ == "__main__":
    comm_count = int(input())
    d = deque()
    for i in range(comm_count):
        sample = (input().split()) 
        if sample[0] == 'append':
            d.append(sample[1])
        elif sample[0] == 'pop':
            d.pop()
        elif sample[0] == 'appendleft':
            d.appendleft(sample[1])
        elif sample[0] == 'popleft':
            d.popleft()
    print(*d) #  * -> extracting deque
        
#end