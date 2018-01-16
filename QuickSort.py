def quickSort(list):
   quickSortHelper(list,0,len(list)-1)

def quickSortHelper(list,first,last):
   if first<last:

       splitpoint = partition(list,first,last)

       quickSortHelper(list,first,splitpoint-1)
       quickSortHelper(list,splitpoint+1,last)


def partition(list,first,last):
   pivotvalue = list[first]

   left = first+1
   right = last

   done = False
   while not done:

       while left <= right and list[left] <= pivotvalue:
           left = left + 1

       while list[right] >= pivotvalue and right >= left:
           right = right -1

       if right < left:
           done = True
       else:
           temp = list[left]
           list[left] = list[right]
           list[right] = temp

   temp = list[first]
   list[first] = list[right]
   list[right] = temp


   return right

list = [54,26,93,17,77,31,44,55,20]
quickSort(list)
print(list)
