#This is a binary search algorithm.
def binary_search (list1, item):
    first = 0
    last = len(list1)-1
    while first <= last:
        middle = (last+first)//2
        if list1[middle]<item:
            first = middle+1
        elif list1[middle]>item:
            last = middle-1
        else :
            return middle

myList = [1,2,3,4,5,6,7,8]
print(binary_search(myList,3))
