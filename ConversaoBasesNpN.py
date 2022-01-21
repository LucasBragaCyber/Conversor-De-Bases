
print("---------- CONVERSAO DE BASES N -> N ----------")
print("De N -> 10")

n_original = str(input("entre com o numero inicial: "))
base_original = int(input("entre com a base do numero inicial: "))
dic = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
dec = 0
dec_temp = list(n_original)
dec_temp.reverse()
for x,i in enumerate(dec_temp):
    dec += dic.index(i) * base_original**(x)

print(f"De base N -> 10: {str(dec)}")

print("De 10 -> N")
b_final = int(input("Entre com a base final: "))
dec1 = dec
#dec = int(input("Entre com o numero decimal: "))
n_final_temp = []
n_final = ''

while True:
    temp_n_final = dec1 % b_final
    n_final_temp.append(temp_n_final)
    if int (dec1/b_final) == 0:
        break
    dec1 = int(dec1/b_final)
n_final_temp.reverse()
for i in n_final_temp:
    n_final += dic[i]
print(f"O numero convertido para a base {b_final} é: {n_final}")