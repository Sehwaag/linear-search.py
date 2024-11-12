position = -1
def search(list,n):
    i = 0
    while(i <= len(list)):
        if list[i] == n:
            globals() ['position']=i
            return True
        i +=1
    return False
list=[3,55,7,8,9,99]
n = 9
if search(list,n):
    print("found at:",position+1)
else:
    print("invalid")
    
