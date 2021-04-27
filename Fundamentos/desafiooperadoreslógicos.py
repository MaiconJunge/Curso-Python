# Desafio Operadores Lógicos

# Os trabalhos
trabalho_terca = True
trabalho_quinta = True

"""
- Confirmando os 2: TV 50' + Sorvete
- Confirmando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""

if trabalho_terca and trabalho_quinta == True:
    print("TV 50' + Sorvete")
elif trabalho_terca != trabalho_quinta:
    print("TV 32' + Sorvete")
else:
    print("Fica em casa!")


# Versão do Professor
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("Tv_50={} Tv_32={} Sorvete={} Saudável={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))
