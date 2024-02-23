class House:
    window=11 
    color="green"
    door=2
    
    def set_door(self,door):
        self.door = door
        
    def get_door(self):
        return self.door
    
ram_ko_ghar=House()
print(ram_ko_ghar.door)
hari_ko_ghar=House()