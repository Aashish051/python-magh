# def hello();
#     print(a)
#     a=11
    
# hello()
# print(a)

# a=10
# def outer():
#     def inner():
#         print('inner sees a as ',a)
#     print('outer sees a as ',a)
#     inner()
    
# print ('global a as',a)
# outer()




# class House:
#     window=11 
#     color="green"
#     door=2
    
#     def set_door(self,door):
#         self.door = door
        
#     def get_door(self):
#         return self.door
    
# ram_ko_ghar=House()
# print(ram_ko_ghar.door)
# hari_ko_ghar=House()



class Burger:
    
    def bun(self):
        print('bun')
        return self
    def cheese(self):
        print ('cheese')
        return self
    def patty(self):
        print('patty')
        return self
    
    
    
burger=Burger()
    
burger.bun().cheese().patty().bun()



# scope use garera global variable login function and check whether credentials are matched return true
    