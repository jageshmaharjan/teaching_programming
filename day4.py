'''
List/Array
'''
arr_1 = []   # initializing the array/list variables eg:; in java AarrayList arr_1 = new AarrayLlist()

print(arr_1)
arr_1.append(500)
print(arr_1)
arr_1.append(333)
arr_1.append(123)
print(arr_1)
arr_1.append("jugs")
print(arr_1)
arr_1.append(12.21)
print(arr_1)
print(len(arr_1))
print(arr_1[1])
print(arr_1[0:3])  #3 returns the array with index from to index sepeaated by :;

print(arr_1[0:2] + arr_1[3:4])  # array with inclusive and exclusive intems // array slicing

print(arr_1)
arr_1.pop(0)  #3 pop keyword will remove the item in the array with given index
print(arr_1)
last_index = len(arr_1)-1  # to get the last index
arr_1.pop(last_index)        #3 removing the last index item
print(arr_1)
'''
tmp_arr1 =  arr_1[0:2]
tmp_arr2 = arr_1[len(arr_1)-1]
print(tmp_arr1 + [999] + [tmp_arr2])
'''