'''
Conditional logic:
  notations:
     == (is equal)
     != (not equal)
     > (greater then)
     < (less than)
     >= (greater or equal to)
     <= (less or equal to)

= (assignment operator)
a = 50
'''



'''
syntax:
if statement:
    run/execute this line
else:
    run/execute this line
'''

# a = 5

# if a > 10:
#     print("a is greater than 10")
# else:
#     print("a is not greater than 10")

# destination = "USA"

# if destination == "Japan":
#     print("take a japanase airline")
# else:
#     print("else do whatever you want")

#----------

extension = "jepg"

if extension == 'jepg':
    print("this is an image file")
else:
    print("this is not an image file")


'''
 Functions/Methods are the defination.
 functions can be used as many times as needed be
 syntax:
    def function_name(parameter1, parameter2):   # you can have as many parameters as you want
        do lot of work
        return results

'''

def add(a, b):   # add is a function name, a and b are the parameters
    return a+b   # a+b is the return results 


result1 = add(30, 40)   # add function is being called with 30 and 40 as a parameters and assigned to varible result
print(result1)

result2 = add(5555555, 222222)
print(result2)


def friends(f1, f2, f3, f4):
    return f1 + " is a good friend of " + f2 + " as well as friend of " + f3 + " but dont forget " + f4

res = friends("tom", "jack", "marry", "harry")
print(res)    


def which_file(extension):
    if extension == "jepg":
        print("this is image file")
    if extension == "docx":
        print("this is word file")
    if extension == "pdf":
        print("this is pdf file")


which_file("docx")



def which_friend(friend):
    if friend == "shabu":
        print("she is smart girl")
    if friend == "rachana":
        print("she is beautiful")
    if friend == "uma":
        print("she is funny friend")


which_friend("uma")