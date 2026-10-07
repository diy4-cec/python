cl1=set()
cl2=set()
n1=int(input("Enter the number of colors in list1: "))
print("Enter the colors for list1:")
for x in range(n1):
    color=input()
    cl1.add(color)
n2=int(input("Enter the number of colors in list2: "))
print("Enter the colors for list2:")
for x in range(n2):
    color=input()
    cl2.add(color)
diff=cl1.difference(cl2)
print("Colors in list1 and not in list2: ",diff)
