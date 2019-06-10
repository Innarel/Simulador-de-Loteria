import random, os

os.system('mode con cols=38 lines=15')
os.system('cls')

print("=== Simulador de Jogos na Loteria ===")
print("")
print("O algoritmo esta tentando ganhar. Aguarde uma pequena eternidade...")
print("Ao final, sera apresentada a quantidade de tentativas e o jogo vencedor.")

lista = []
jogo = []
sorteio = []
qtd = 0
quadra = 0
quina = 0
acertos = 0
atualiza = 0

def crialista():
	
	lista.clear()
	for i in range(1,61):
		lista.append(i)

def joga():
	
	jogo = [4,8,15,16,23,42]
	sorteio = [2]
	qtd = 0
	quadra = 0
	quina = 0
	acertos = 0
	atualiza = 0	

	while jogo != sorteio:

		#Descomente para jogar com numeros aleatorios
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
		
		acertos = 0
		for i in range(6):
			if sorteio[i] in jogo:
				acertos = acertos + 1
				
		if acertos == 4:
			quadra = quadra + 1
			atualiza = 1
				
		if acertos == 5:
			quina = quina + 1
			atualiza = 1


	
		if atualiza == 1:
			os.system('cls')
			print("=== Simulador de Jogos na Loteria ===")
			print("")
			print("O algoritmo esta tentando ganhar.\nAguarde uma pequena eternidade...")
			print("")
			print('Aposta: '+str(jogo))
			print('Sorteio: '+str(sorteio))
			print('')
			print('Quadras: ',quadra)
			print('Quinas: ',quina)
			print('')
			print('Tentativas: '+str(qtd))
			atualiza = 0

joga()
