if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

myList = []

for i in arr:
    if i not in myList:
        myList.append(i)

myList.sort()

print(myList[-2])