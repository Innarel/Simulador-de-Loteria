import random, os

os.system('cls')

print("=== Simulador de Jogos na Loteria ===")
print("")
print("O algoritmo esta tentando ganhar. Aguarde uma pequena eternidade...")
print("Ao final, sera apresentada a quantidade de tentativas e o jogo vencedor.")

lista = []
jogo = []
sorteio = []
qtd = 0

def crialista():
	
	lista.clear()
	for i in range(1,61):
		lista.append(i)

def joga():
	
	jogo = [4,8,15,16,23,42]
	sorteio = [2]
	qtd = 0	

	while jogo != sorteio:

		# Descomente para jogar com numeros aleatorios
		#crialista()
		#jogo.clear()
		#for i in range(6):
			#jogo.append(lista.pop(random.randrange(0,len(lista))))

		crialista()
		sorteio.clear()
		for i in range(6):
			sorteio.append(lista.pop(random.randrange(0,len(lista))))

		jogo.sort()
		sorteio.sort()

		qtd += 1

	os.system('cls')

	print(jogo)
	print(sorteio)
	print('')
	print(qtd)

joga()
