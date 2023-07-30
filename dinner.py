#All Pets
pets = {

#Pet 1 
    'oscar' : {
        'Animal': 'Cat',
        'Owner': 'Nana'
    },

#Pet 2
    'gaddy' : {
        'Animal': 'Gator',
        'Owner': 'Tanos'

    },
#Pet 3
    'watty' : {
        'Animal': 'Fish',
        'Owner': 'Lizzy'   

    }

}

for pet, pet_info in pets.items():
    print(f"\nPet: {pet.title()}")
    animal = f"{pet_info['Animal']}"
    owner = f"{pet_info['Owner']}"
    
    print(f"\tAnimal: {animal.title()}")
    print(f"\tOwner: {owner.title()}")


