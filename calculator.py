def start():
	metod = input("Выберите (+ - * /) ")

	a = input("Введите первое число: ")
	b = input("Введите второе число: ")

	a = int(a)
	b = int(b)

	if metod == "+": print(a + b)
	elif metod == "-": print(a - b)
	elif metod == "*": print(a * b)
	elif metod == "/": print(a / b)
	else: print("Выберите (+ - * /)")

	again = input("Ещё вычесление ? (yes) or (no) ")
	if again == "yes": start()
	else: return

start()

