# Question1
def convert(farheniet):
    celsius = (farheniet-32)*5/9
    return print('Temperature in degree celsius is',celsius)
convert(98)



# Quetion2
def convert(seconds):
    min =int(seconds/60)
    sec =seconds%60
    return print (min,'minutes','and',sec,'seconds')
n=3800
print(convert(n))
    

# Question3
list =[2,5,7,4,9,1]
print('Length of list is',len(list))
print ('First element of list is',list[0])
print('Fourth element of list is',list[4])


# Question4
list =[3,6,8,4,1]
def remove(number):
   list.remove(number)
print('After removal',list)

remove(4)


def append(number):
   list.append(number)
   print('After append',list)

append(9)


def pop(number):
    list.pop(number)
    print('After pop',list)
pop(2)



# Question5
list=[2,4,6,8,1]
total =sum(list)
print(total)

# Question6
def common(a, b): 
    a_set = set(a) 
    b_set = set(b) 
  
    if (a_set & b_set): 
        print(a_set & b_set) 
    else: 
        print("No common elements")  
           
   
a = [1, 2, 3, 4, 5,6] 
b = [5, 6, 7, 8, 9] 
common(a, b) 


# Question7
str = input('Enter the string ')
print(len(str))



# Question8
def prime(number):
    for num in range(2,number):
        for i in range(2,num):
            if num % i == 0:
                 break
        else:
          print(num)
           
prime(100)



# Question9
def palindrome(s):
    return s == s[::-1]
s=input('enter the string ')
str =palindrome(s)
if str:
    print('palindrome')
else:
        print('Not palindrome')



# Question10
s = "pineapple"
def char_frequency(s):
    dict = {}
    for n in s:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

counts = char_frequency(s)
print(counts)

 
   

    
    
