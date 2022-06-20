# TOdo: create two arrays, with 5integer  items AND 5 STRING ITEMS, REMOVE 1ST ITEM FROM 1ST ARRY AND REMOVE LAST ITEM FROM 2ND ARRAY AND MERGE THEM
myarr1 = []
myarr1.append(100)
myarr1.append(102)
myarr1.append(110)
myarr1.append(320)
myarr1.append(456)

myarr2 = []
myarr2.append("jugs")
myarr2.append("avi")
myarr2.append("ankita")
myarr2.append("rachana")
myarr2.append("shabu")

myarr1.pop(0)
myarr2.pop(len(myarr2)-1)

final = myarr1 + myarr2
print(final)