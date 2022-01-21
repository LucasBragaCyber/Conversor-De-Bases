print("-------- Conversao de base N -> 10 --------")

n_original = str(input("entre com o numero original: "))                    #Numero de base N a ser convertido
base_original = int(input("entre com a base do numero digitado(N): "))      #Base N
dic = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']     #Lista dicionario com os valores possiveis para bases e numeros
dec = 0                                                                     #Valor inicial do numero de base 10
dec_temp = list(n_original)
dec_temp.reverse()
for x,i in enumerate(dec_temp):                                             #Permite um loop sobre o objeto iterador e mantem uma contagem de quantas iterações ocorreram.
    dec += dic.index(i) * base_original**(x)                                #Faz uma varredura na Lista Dicionario, para entao calcular corretamente um numero de base N para Base 10.
print(f"O numero {n_original} de base {base_original} convertido para decimal, é: {str(dec)}")


