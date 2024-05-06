# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.
#     class Vehicle:
#         def __init__(self, reg_num, type, owner):
#             self.registration_number = reg_num
#             self.type = type
#             self.owner = owner
# Expected Outcome: Completion of the Vehicle class with the update_owner method and 
# a demonstration script showing the creation of Vehicle objects and updating their owners.


class Vehicle():
    def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

    def change_owner(self, new_owner):
        self.owner = new_owner

car1 = Vehicle('REDPPR', 'SUV', 'Harsh')
car2 = Vehicle('YSOBLU', 'EV', 'Harsh')

print(f'{car2.owner} is the owner of a {car2.type} with registration number {car2.registration_number}')


#Changing Owner Name

car2.change_owner('Dylan')

print(f'{car2.owner} is the owner of a {car2.type} with registration number {car2.registration_number}')
