# def Fib():
#     a = 0
#     b = 1
#     while True:
#         a,b = b,a+b
#         yield a

# for each in Fib():
#     if each > 100:
#         break
#     else:
#         print(each)


# a = [x for x in range(10) if not (x % 2) and x % 3] 
# print(a)

# b = {i: i % 2 == 0 for i in range(10)}
# print(b)

# c = {i for i in [1,2,3,1,2,4,5,6,7]}
# print(c)

# d =sum(i for i in range(100) if i % 2 == 0)
# print(d)



# import math

# def get_primers(input_list):
#     return (element for element in input_list if is_prime(element))

# def is_prime(number):
#     if number > 1:
#         if number == 2:
#             return True
#         if number % 2 == 0:
#             return False
#         for current in range(3,int(math.sqrt(number)+ 1),2):
#             if number % current == 0:
#                 return False
#         return True
#     return False 

# list1 = [1,2,3,4,5,64,8,8,9,45]
# for i in get_primers(list1):
#     print(i)

# import math

# def get_primes(number):
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1

# def is_prime(number):
#     if number > 1:
#         if number == 2:
#             return True
#         if number % 2 == 0:
#             return False
#         for current in range(3,int(math.sqrt(number)+ 1),2):
#             if number % current == 0:
#                 return False
#         return True
#     return False 

# def solve_number_10():
#     # She *is* working on Project Euler #10, I knew it!
#     total = 2
#     for next_prime in get_primes(3):
#         if next_prime < 200:
#             total += next_prime
#         else:
#             print(total)
#             return

# solve_number_10()




# def Myrev(data):
#     for each in range(len(data) - 1,-1,-1):
#         yield data[each]

# for i in Myrev("xiaoniu"):
#     print(i,end = "")



import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3,int(math.sqrt(number) + 1),2):
            if number % current == 0:
                return False
        return True
    return False

def get_primers(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve():
    total = 2
    for next_primer in get_primers(3):
        if next_primer < 2000000:
            total += next_primer
        else:   
            print(total)
            return 

if __name__ == "__main__":
    solve()
    



