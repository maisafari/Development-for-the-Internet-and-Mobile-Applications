poema = '''Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho /
Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo /
Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito /
Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito /
Precisa ser muito sincero e claro / Pra confessar que andei sambando errado /
Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado /
Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente /
Isso me deixa triste e cabisbaixo / Por isso eu fiz um samba bem pra frente /
Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente /
E coerentemente assino embaixo / Hoje é preciso refletir um pouco /
E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco /
Pra contestar e pra botar defeito / Precisa ser muito sincero e claro /
Pra confessar que andei sambando errado / Talvez precise até tomar na cara /
Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho /
Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo'''

novos_versos = '''Por isso eu fiz um samba bem pra frente
Dizendo realmente o que é que eu acho
Isso me deixa triste e cabisbaixo'''

#a
versos_poema = poema.split('/')
for verso in versos_poema:
   print(verso)
print()

#b

poema_completo = versos_poema + novos_versos.split("\n")
for verso in poema_completo:
   print(verso)
print()

#c

for verso in poema_completo[-2:]:
  print(verso)

#d
num = 0
for verso in poema_completo:
   if str(verso).count("samba") >= 1:
       num = num + 1
print(num)

#e

vogais = ["a", "e", "i", "o","u"]
for v in vogais:
    print(str(v) +": " + str(str(poema_completo).count(str(v))))

#3.2
#a
disciplinaAnoPassado={
  "AED": 15,
  "POO": 20,
  "IP":19
}

disciplinaEsteAno={
    "CDSI": 17,
    "Econ": 18,
    "DIAM":14
}
print(disciplinaAnoPassado, disciplinaEsteAno)

#b
disciplinaEsteAno.update(disciplinaAnoPassado)
print(disciplinaEsteAno)

#c
print(disciplinaEsteAno.keys())

#d
print(disciplinaEsteAno.values())

#e
print(dict(sorted(disciplinaEsteAno.items())))


class GestDiscipliinas:

    #f
    def exists( self, dictionary,myStrinng):
        if myStrinng in dictionary:
            print(discipline + " existe no dicionario")
     #g
    def valueGreaterThan(self,dictionay,myValue):
        notasAltas = []
        for key, nota in dictionay.items():
            if myValue < nota:
                notasAltas.append(key)
        return notasAltas

 #h Calcular a média das notas das disciplinas presentes no dicionário

    def media(self,dictionary):
        media = 0
        for key,nota in dictionary.items():
            media = media + nota
        media = media/ len(dictionary)
        return media

#i Obter a lista das três disciplinas com as melhores notas
    def high(self, dictionary):
        notasMaisAltas = []
        sorted(dictionary.items(), key=lambda x: x[1])
        notasMaisAltas= sorted(dictionary.items(), key=lambda x: x[1])[-3:]
        return notasMaisAltas
        



manage = GestDiscipliinas()
discipline = "DIAM"
manage.exists(disciplinaEsteAno,discipline)
nota = 17
print(manage.valueGreaterThan(disciplinaEsteAno,nota))
print(manage.media(disciplinaEsteAno))
print(manage.high(disciplinaEsteAno))

#3.3
# Selection sort in Python

def selectionSort(array, size):

	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9,88,-90,-202,747, 1000, 3, 5, 7]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)

#3.4 Estruturas de controlo

class Transpor:
    def possivelTransporOpcao1(self, palavra1, palavra2):
        if len(palavra1) != len(palavra2):
             return False
        palavra2List  =  list(palavra2)
        for letra in list(palavra1):
            if letra in palavra2List:
                palavra2List.remove(letra)
        if len(palavra2List) == 0:
            return True
        return False
    def possivelTransporOpcao2(self,palavra1,palavra2):
        if len(palavra2)!= len(palavra1):
            return False
        palavra1List = list(palavra1).sort()
        palavra2List = list(palavra2).sort()
        if palavra1List == palavra2List:
            return True
        return False

transpor = Transpor()
#a
print(transpor.possivelTransporOpcao1("roma", "amor"))
print(transpor.possivelTransporOpcao2("roma", "amor"))
