#imports ninja, pet, and sub_pet classes
import classes

#creates a cat and dog instance
garetts_cat  = classes.Cat("fluffy", 50, 50)
garetts_dog  = classes.Dog("shadow", 50, 50)
# garetts_pet = classes.Pet("jynx", 50, 50)

#creates ninja instance
garett = classes.Ninja("Garett", garetts_cat, "cat")

#performs actions
garett.walk()
garett.feed()
garett.bathe()
garetts_cat.sleep()
