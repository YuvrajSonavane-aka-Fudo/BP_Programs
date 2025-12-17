string1 = "_abc a_der der_ kdfj "

def underScore(str1):
    list1 = []
    str1 = list(str1.split(" "))
    for i in str1:
        if "_" in i:
            list1.append(i)
    print(list1)

underScore(string1)