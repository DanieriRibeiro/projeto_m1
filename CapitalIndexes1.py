print ("Olá!\nTudo bem?\nResponda s ou n")
a1 = input()

if a1 == 's':
  print ("\nQue ótimo!")
elif a1 == 'n':
  print ("\nQue pena :( mas tudo vai melhorar!")
else:
  print ("\nNão entendi, mas precisamos seguir,")
  

def capital_indexes(str1):
    return [tamanho for tamanho in range(len(str1)) if str1[tamanho].isupper()]

s1 = input("Vamos para a execução!\n\nEscreva uma palavra que tenha alguma letra maiúscula para retornar as suas respectivas posições: \n")

print("\n\nAs posições são:")
print(capital_indexes(s1))
print("\nMuito Obrigada!")