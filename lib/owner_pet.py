class Pet:
<<<<<<< HEAD
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # Initialize owner attribute to None
        if owner is not None:
            self.set_owner(owner)  # Set the owner using set_owner method if provided
        Pet.all_pets.append(self)

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Invalid owner type: owner must be an instance of Owner")
        self.owner = owner
        owner.add_pet(self)  # Add pet to owner's list
=======
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        print("GETTING _pet_type")
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, new_pet_type):
        print("SETTING _pet_type")
        Hell = Exception
        if new_pet_type not in Pet.PET_TYPES:
            raise Hell(f"{new_pet_type} not in pet types")
        else:
            self._pet_type = new_pet_type
>>>>>>> ad5b60422914f1cb178c22393b5be5652bc31456

class Owner:
    def __init__(self, name):
        self.name = name
<<<<<<< HEAD
        self.pet_list = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type: pet must be an instance of Pet")
        self.pet_list.append(pet)
        pet.owner = self

    def remove_pet(self, pet):
        self.pet_list.remove(pet)
        pet.owner = None

    def pets(self):
        return self.pet_list

    def get_sorted_pets(self):
        return sorted(self.pet_list, key=lambda pet: pet.name)
=======

    def pets(self):
        return [ pet for pet in Pet.all if pet.owner == self ]
    
    def add_pet(self, new_pet):
        if isinstance(new_pet, Pet):
            new_pet.owner = self
        else:
            raise Exception("NO")
    
    def get_sorted_pets(self):
        my_pets = self.pets()
        sorted_pets = sorted( my_pets, key = lambda each_pet: each_pet.name.lower() )
        return sorted_pets
>>>>>>> ad5b60422914f1cb178c22393b5be5652bc31456
