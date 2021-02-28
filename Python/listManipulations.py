"""
author : Enes Çavuş
subject : understanding list functions
date : 23 Feb 2021
goal : to practice list functions and solve hackerrank questions/problems
sources : https://www.hackerrank.com/dashboard
"""
 # there must be a specific input entry for this code 
 # this code specified for hacerrank sample input

if __name__ == '__main__':
    N = int(raw_input())
    mainList = []
    for i in range(N):
        command = list(raw_input().split())
        if command[0] == 'print':
            print(mainList)
        elif command[0] == 'pop':
            mainList.pop()
        elif command[0] == 'reverse':
            mainList.reverse()
        elif command[0] == 'sort':
            mainList = sorted(mainList)
        elif command[0] == 'insert':
            mainList.insert(int(command[1]), int(command[2]))
        elif command[0] == 'remove':
            mainList.remove(int(command[1]))
        elif command[0] == 'append':
            mainList.append(int(command[1]))


# end