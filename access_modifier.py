class Person:
    
    def __init__(self,name,age,password) -> None:
        self.name=name
        self.age=age
        self.password=password
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password=password
    
    
    
    # def set_password(self,password):
    #     self._password=password
        
    # def get_password(self):
    #     return self._password
        
        
person=Person('name',12,'password')

# print(person.name)
# print(person._age)
# print(person._password)

print(person.password)
        
