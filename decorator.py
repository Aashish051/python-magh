# # def star(func):
# #     def wrapper():
# #         print ('*'*10)
# #         func()
# #         print('*'*10)
# #     return wrapper
    
# # def hello():
# #     print('hello')
    
# # star(hello)()


# # def sum (a,b):
# #     print (a+b)
    
# # sum (1,2)

# def func(n):
#     return lambda x:x*n
# tripler=func(3)
# print(tripler(4))  



def my_range(start, stop, step):
    print(start)
    start+=step
    if start>stop:
        return 0
    else:
        my_range(start,stop,step)        
my_range(1,10,2)