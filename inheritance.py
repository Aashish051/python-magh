# class grandfather: 
#     house="good house"
    
# class father (grandfather):
#     car="lambo"
    
# class mother:
#     jewellery="god necklace"
    
# class son(father,mother):
#     console="ps5"
    
# son=son()
# print (son.console)


class Grandfather: 
    def __init__(self):
        print("I am grandfather")
    house="good house"
    
class Father (Grandfather):
    car="lambo"
    
class Mother:
    jewellery="god necklace"
    
class Son(Father,Mother):
    console="ps5"
    
    def __init__(self)->None:
        print(self.console)
        super().__init__()
    
son=Son()
print(son.console)

