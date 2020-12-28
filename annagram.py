one = []; two = []

qus_one = input("Введите первое слово ")
qus_two = input("Введите второе слово ")

for i in qus_one: one.append(i)
for i in qus_two: two.append(i)
	
def sorted():
	one.sort()
	two.sort()
	if one == two: print(True)
	else: print(False)

sorted()

