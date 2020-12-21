my_tuple = ("Аллаберидин", "Дамир", 19)

people = []
people.append(my_tuple)
print(people)

tuple1 = ("Алексеев", "Алексей", 21)
people.append(tuple1)

tuple2 = ("Миронов", "Александр", 20)
people.append(tuple2)

tuple3 = ("Тихонова", "Таня", 18)
people.append(tuple3)

tuple4 = ("Щедрова", "Екатерина", 22)
people.append(tuple4)

print(people)
list.sort(people)

print("Отсортированный список: ")
print(people)
