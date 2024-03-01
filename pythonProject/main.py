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
#for verso in versos_poema:
#   print(verso)
#print()

#b

poema_completo = versos_poema + novos_versos.split("\n")
#for verso in poema_completo:
#   print(verso)
#print()

#c

#for verso in poema_completo[-2:]:
#    print(verso)

#d

#num = 0
#for verso in poema_completo:
 #   if str(verso).count("samba") >= 1:
 #       num = num + 1
#print(num)

#e

#vogais = ["a", "e", "i", "o","u"]
#for v in vogais:
#    print(str(v) +": " + str(str(poema_completo).count(str(v))))

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
#print(disciplinaAnoPassado, disciplinaEsteAno)

#b
disciplinaEsteAno.update(disciplinaAnoPassado)
#print(disciplinaEsteAno)

#c
#print(disciplinaEsteAno.keys())

#d
#print(disciplinaEsteAno.values())

#e
#print(dict(sorted(disciplinaEsteAno.items())))


class gestDiscipliinas:

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
        



manage = gestDiscipliinas()
discipline = "DIAM"
#manage.exists(disciplinaEsteAno,discipline)
nota = 17
#print(manage.valueGreaterThan(disciplinaEsteAno,nota))
#print(manage.media(disciplinaEsteAno))
print(manage.high(disciplinaEsteAno))

