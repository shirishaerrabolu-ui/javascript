print("===== TUPLE OPERATIONS =====")

tuplex = (10, "Hello", 5.5, True)
print("Mixed Tuple:", tuplex)

tuplex = (1, 2, 3, 4, 5, 6)
print("Original Tuple:", tuplex)

tuplex = tuplex + (9,)
print("After Adding 9:", tuplex)

tuple1 = (50, 20, 50, 30, 50, 40)
print("50 appears", tuple1.count(50), "times")

tuplex = (10, 20, 30, 40, 50, 60, 70, 80)
print("Original Tuple:", tuplex)

print("Slice [3:5]:", tuplex[3:5])
print("Slice [:6]:", tuplex[:6])

print("Length of Tuple:", len(tuplex))
print("Item at Index 0:", tuplex[0])
print("Last Item:", tuplex[-1])