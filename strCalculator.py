def strToInt(strList):
    for i in strList:
        strList[strList.index(i)] = int(i)
    return strList


def subSum(dataList, isMinusExist):
    sum = 0
    if isMinusExist:
        for i in dataList:
            if i == dataList[0]:
                sum -= i
            else:
                sum += i

    else:
        for i in dataList:
            sum += i
    return sum

def calSentence(data):
    result = 0
    splitMinus = data.split('-')
    if(splitMinus[0] == ''):
        # if first data is smaller than 0
        splitMinus.pop(0)
        for i in splitMinus:
            splitPlus = i.split('+')
            intData = strToInt(splitPlus)
            result += subSum(intData, True)
    else:
        isFirst = True
        for i in splitMinus:
            splitPlus = i.split('+')
            intData = strToInt(splitPlus)
            if isFirst:
                isFirst = False
                result += subSum(intData, False)
            else:
                result += subSum(intData, True)
    return result


inputData = input("Enter Data: ")
print(calSentence(inputData))
