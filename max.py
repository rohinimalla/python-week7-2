lst=[]
z=int(input("enter size of list:"))
print("entre elements:")
for i in range(0,z):
    lst.append(int(input("")))
x=min(lst)
y=max(lst)
print("minimum element in the list:",x)
print("maximum element in the list:",y)
