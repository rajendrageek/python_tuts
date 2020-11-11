num = 10
print(str(num).ljust(10, "0"))

lst = [1, 2, 3, 4, 5, 6]

x = lst.pop()
print(lst)



n = int (input("enter the lenght of the list"))
lst1 = []

for i in range(n):
    element = int(input())
    lst1.append(element)

print("list elements are:", lst1)
