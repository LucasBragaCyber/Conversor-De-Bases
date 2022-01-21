print(" ----------- CONVERSAO DE BASES 10 -> N -----------")

b_final = int(input("Entre com a base final: "))
dec = int(input("Entre com o numero decimal: "))
dic = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
n_final_temp = []                                                            #Array vazio, para entao ser preenchido com um valor correto posteriormente
n_final = ''                                                                 #String vazia, para entao ser preenchida posteriormente

while True:
    temp_n_final = dec % b_final                                             # Calculo da divisao, do numero decimal pela base final (base da conversao),onde sera retornado o resto da divisao
    n_final_temp.append(temp_n_final)                                        #Atribui o valor do resultado de temp_n_final ao n_final_temp (que até entao era uma Array vazia)
    if int (dec/b_final) == 0:
        break
    dec = int(dec/b_final)
n_final_temp.reverse()                                                      #Inverte o resultado, que sao os valores do resto da divisao do numero pela base a ser convertida
for i in n_final_temp:
    n_final += dic[i]
print(f"O numero decimal convertido para a base {b_final} é: {n_final}")