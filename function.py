# def hello(f_name,m_name,L_name):
#     print(f'$$hello,{f_name} {m_name} {L_name}$$')
#     return 1
# a=hello(m_name='bdr',f_name='ram',L_name='smth')
# print (a)


# def person(*names):


    
#     for name in names:
#         print (f"hello,{name}")
        
# person('ram','shyam',1,2,3,4)
    
    
# def person (**attrs):
#     print (attrs['name'], attrs['age'])
    
# person (name='shyam',age=9)


# def number(n=1):
#     print (n)
#     if n==10:
#         return
#     number(n+1)
    
# number ()


# function in calculator. sum in return type
# range function using recursion

# def add(a, b):
#     result = a + b
#     return result

# sum_result = add(3, 5)
# print(sum_result) 


# print(list(range(1,10,2)))

# def recursive_range(n, current=0):
#     if current == n:
#         return []
#     else:
#         return [current] + recursive_range(n, current + 1)

# # Test the function
# print(recursive_range(10))

def recursive_range(start, end, step=1):
    if start >= end:
        return []
    else:
        return [start] + recursive_range(start + step, end, step)

print(recursive_range(1, 20, 2))


