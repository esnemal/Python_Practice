
maths=input('maths=')
print ('type of maths=', type(maths))
maths=int(maths)
print ('type of maths=', type(maths))
sci=input('sci=')   #take input as string
sci=int(sci)      #type casting string to int


if maths>=90 and sci>=90:
    print("exellent")
elif ((maths<90 and maths>=60) and (sci<90 and sci>=60)):
    print("average")
elif maths<60 and sci<60:
    print("need improvment")
else:
    print("study more")
