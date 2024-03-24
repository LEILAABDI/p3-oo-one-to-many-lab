class Pet:
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

class Owner:
    def __init__(self, name):
        self.name = name
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
