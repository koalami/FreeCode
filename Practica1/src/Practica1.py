#Trabajaremos en un codigo para control de versiones de git desde VS..
class person:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.partner = None
        self.children = []
        
    def add_partner(self, partner: 'person'):
        if self.partner is not None:
            print(f"{self.name} ya tiene una pareja: {self.partner.name}")
        else:
            self.partner = partner
            partner.partner = self.name
            print(f"{self.name} y {partner.name} se unen como pareja")
            
            
    def add_child(self, child: 'person'):
        if self.partner == None:
            print(f"se necesita una pareja")
            
        elif child not in self.children:
            self.children.append(child)
            self.partner.children.append(child)
            print(f"{self.name} y su pareja {self.partner.name}han tenido a {child.name} como hijo")
           
        else:
            print(f"{self.name} ya tiene a {child.name} como hijo")
            

# Creamos la logica del arbol genealogico
class FamilyTree:
    def __init__(self):
        self.people = {}
        
    def add_person(self, id: int, name: str):
        if id in self.people:
            print(f"La persona con id {id} ya existe")
        else:
            person = person(id, name)
            self.people[id] = person
            print(f"la persona con id {id} y name {name} ha sido añadida al arbol")
    def remove_person(self, id: int, name: str):
        if id in self.people:
            person = self.people[id]
            del self.people[id]
            print(f"La persona con id {id} y name {name} ha sido eliminada del arbol")
        else:
            print(f"La persona con id {id} y name {name} no existe en el arbol")
    def set_parter(self, id1: int, id2: int, name: str):
        if id1 in self.people and id2 in self.people:
            person1 = self.people[id1]
            person2 = self.people[id2]
            person1.add_partner(person2)
        else:
            print(f"Alguna de las personas con ids {id1} y {id2} no existen en el arbol")
   
   
   
    def add_child(self, parent_id: int, parent_name: str, child_id: int, child_name: str):
        if parent_id in self.people and child_id in self.people:
            if parent_id == child_id:
                print("No se puede agregar a un hijo a una persona que sea su propio hijo")
            else:
                parent = self.people[parent_id]
                child = self.people[child_id]   
                parent.add_child(child)
        else:  
            print(f"Alguna de las personas con ids {parent_id} y {child_id} no existen en el arbol")
    
    def print_tree(self):
        pass
    