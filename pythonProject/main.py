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

ultimos_versos = versos_poema_completo[-2:]

for verso in ultimos_versos:
    print(verso)