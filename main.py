import ManagementSystem as ms

if __name__ == "__main__":
  a1 = ms.Animal('Bob', 'Tiger', 1)
  a2 = ms.Animal('Jane', 'Lion', -1)
  a3 = ms.Animal('John', 'Weasel', 3)
  a4 = ms.Animal('Jill', 'Mink', 11)
  a5 = ms.Animal('Jack', 'Ermine', 6)
  a6 = ms.Animal('Jean', 'Tanuki', 11)
  # create 8 more animals "Populate your structures with at least 10 sample animals."
  basic_care = ms.CareFacility(1, 3)
  advanced_care = ms.CareFacility(4, 7)
  intensive_care = ms.CareFacility(8, 10)

  # do stuff here
  basic_care.intakeAnimal(a1)
  basic_care.intakeAnimal(a2)
  basic_care.intakeAnimal(a3)
  basic_care.decreaseCareLevel()
  for animal in basic_care.dischargeAnimals():
    print(animal)

  a1.care = 1
  a2.care = 2
  basic_care.intakeAnimal(a1)
  basic_care.intakeAnimal(a2)
  basic_care.increaseCareLevel()
  basic_care.increaseCareLevel()
  for animal in basic_care.escalateAnimals():
    print(animal)