def maxnum(n):
n = int(input("Enter the size of an array"))
list = [int(input()) for x in range(n)]
max = list[0]
for i in range(0,len(list)):
if list[i] > max:
max = list[i]

print("max num in the given list is ", +str(max))
print(maxnum(5)
