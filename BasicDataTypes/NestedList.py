if __name__ == '__main__':
    myList = list()
    myFloatList = list()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        myList.append([name, score])
        myFloatList.append(score)

    myFloatList = list(set(myFloatList))
    myFloatList.sort(reverse=True)
    second = myFloatList[-2]

    myList.sort()

    for i in myList:
        if i[1] == second:
            print(i[0])

