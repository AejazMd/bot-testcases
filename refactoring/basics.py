def reverseList():
    """ Reverse a list """
    sampleList = [1, 2, 3, 4, 5]
    for i in range(len(sampleList)):
        print(sampleList[len(sampleList)-1-i])

if __name__ == '__main__':
    reverseList()