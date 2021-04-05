def bubble_sort(array):
    for i in range(1,len(array)):
        for a in range(len(array)-i):
            if array[a]>array[a+1]:
                b = array[a]
                array[a] = array[a+1]
                array[a+1] = b
    return array 

sayilar = [1,1,3,4,56,78,78,9,54,54]
print("{}".format(bubble_sort(sayilar)))           