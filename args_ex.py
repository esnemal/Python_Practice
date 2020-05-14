import sys

args=sys.argv
print("type of args:", type(args))
print("type od arge variable",type(args[1]))
for i in args:
    print(i)
sum=int(args[1])+int(args[2])
print("sum=",sum)
