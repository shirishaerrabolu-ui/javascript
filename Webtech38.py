import array as arr

basket1 = {"Apple", "Banana", "Orange"}
basket2 = {"Mango", "Grapes", "Orange"}


basket1.add("pineapple")
print("Basket 1:", basket1)
print("Common fruits: ", basket1.intersection(basket2))


fruits = arr.array('i', [3, 5, 3, 7])
fruits.insert(1, 4)
fruits.append(6)

print("Fruit counts:", fruits.tolist())
print("Count of 3:", fruits.count(3))

fruits.reverse()
print("Reversed array:", fruits.tolist())

