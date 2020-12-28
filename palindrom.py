data = []; newData = []

qus_txt = input("Введите слово для проверки ")

for i in qus_txt:
	data.append(i)
	newData = data.copy()
	
def check():
	data.reverse()
	if data == newData: print(True)
	else: print(False)
	
check()