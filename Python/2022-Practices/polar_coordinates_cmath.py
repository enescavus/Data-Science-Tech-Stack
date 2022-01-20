# polar coordinates - quick solution for hackerrank python practices
# more information about polar funciton and polar coordinates
# -- > https://www.w3schools.com/python/ref_cmath_polar.asp
# check hackerrank for more detail about challanges
# @date : jan 2022


from cmath import polar

# Convert a complex number to polar coordinates form
inp = complex(input().strip())
out = polar(inp)
print(out[0])
print(out[1])

# output like
# first coordinate of the converted complex number
# second coordinate of the converted complex number

# end line - Enes
