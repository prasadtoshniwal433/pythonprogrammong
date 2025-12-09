print("hello world")



arr=[10,20,3,40,50,60,7]


print(len(arr))
num=int(input("enter the element you have to search into the array"))
flag= True

for i in range(len(arr)):
    if arr[i]==num:
        flag=False
        # print(f"the element {num} is found at index {i}")
        break
    else:
        continue


if flag==True:
    print(f"the element {num} is not found in the array")
else:
    print(f"the element {num} is found at index {i}")