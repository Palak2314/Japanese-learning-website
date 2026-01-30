# n = 0
# while n <= 1000:

#     num = str(n)
#     length = len(num)
#     sum = 0
#     for digit in num:

#         sum += int(digit) ** length

#     if sum == n:
#         print(n) 

#     n +=1


# str = input("enter a string")
# if str == str[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")







# i = 0
# while i <= 100:
        
#     if i % 2 == 0:
#         print(f"{i} is prime")
#     i = i + 1 





    # while j<0:
    #     j = j * j
    # j = j - 1
    






# n = int(input("enter the no."))

# fact = 1
# while n > 1:
#     fact *= n
#     n = n - 1
# print(fact)


# str = "I love PCU"

# print(str[0:11])
# print(str[0:len(str)])
# print(str[0:len(str):2])
# print(str[len(str):-1])



# n = int(input("enter the digit"))
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")


# i = int(input("enetr 1st digit"))
# j = int(input("enetr 2nd digit"))
# k = int(input("enetr 3rd digit"))

# if i > j and i > k:
#     print(f"{i} is greatest among all")
# elif i < j and j > k:
#     print(f"{j} is greatest among all")
# else:
#     print(f"{k} is greatest among all")



# list methods:

l = ["pcu","has","best","teachers"]
# slice
print(l[1:len(l)])
# appned method
l.append("420")
print(l)
# insetr at a position
l.insert(3,"hello pcu")
print(l)
# remove 
l.remove("hello pcu")
print(l)
#pop
l.pop(4)
print(l)
#sort fun
ln = [2,6,1,23,99,11,231,0]
ln.sort()
print(ln)
#rev fun
l.reverse()
print(l)

 


# set functions

s1 = {1,2,3,61,383}
s2 = {2,44,64,123,11,1,3}

# add function
s1.add(22)
print(s1)
#remove function
s1.remove(383)
print(s1)
# union function
print(s1.union(s2))
# intersection function
print(s1.intersection(s2))



# tuple methods

t = (1,2,3,4,5,6,7)
# count
print(t.count(111))
# index
print(t.index(6))
print(sum(t))


# dictionary methods



marks = {
    "yogesh" : 100,
    "ranjit" : 99,
    "ronak":100,
    "sarthak_bhaiii":10000
}


print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"ranjit":100})
print(marks.items())
print(marks.get("ronak"))


# string methods 


string = "i love pcu"

print(string.endswith("22"))
print(string.startswith("i"))
print(string.capitalize())
print(string.title())
print(string.replace("i", "everyone"))
print(len(string))
















