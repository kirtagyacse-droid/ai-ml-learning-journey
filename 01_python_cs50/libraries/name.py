import sys
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# if len(sys.argv) <2:
#     print("too few arguments")
# elif len(sys.argv) >2:
#     print("too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])


# if len(sys.argv) <2:
#     sys.exit("too few arguments")
# elif len(sys.argv) >2:
#     sys.exit("too many arguments")

# print("hello, my name is", sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# for arg in sys.argv:
#     print("hello, my name is",arg)

# the output of the above will be:
# python name.py kirtagya yadav bichwaliya
# hello, my name is name.py
# hello, my name is kirtagya
# hello, my name is yadav
# hello, my name is bichwaliya

if len(sys.argv)<2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
