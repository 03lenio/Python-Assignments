x = "[1,2,3,4, [a,b,c,d], help, run, [[a,b],[1,2]]]\n"
# Ex. a
x = x.strip("\n")
# Ex. b
x = x.replace("[", "", 1)
x = "".join(x.rsplit("]", 1))
print(x)
# Ex. c
print(x.find("[a,b]"))
# Ex. d
print(x.replace("2", "1234"))