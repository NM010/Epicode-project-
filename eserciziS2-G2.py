"""
l_serbatoio = float(input("inserire litri nel serbatoio:"))
e_benzina = float(input("inserire efficienza km/l: "))
p_benzina = float(input("inserire prezzo per litro: "))

c_benzina = (100 / e_benzina ) * p_benzina
d_benzina = e_benzina * l_serbatoio
print("costo per 100 km: " , c_benzina)
print("puoi percorrere ancora: " , d_benzina)

"""

"""

metri = float(input("inserisci misura in metri: "))

piede = metri * 3.281
pollice = metri * 39.37
miglia = metri / 1609



print(piede, "piedi")
print(pollice, "pollici")
print(miglia, "miglia")

"""


"""
string = input("scrivi una frase: ")
first_3 = string[0:3]
last_3 = string[-3:]
puntini = " ... "

concatena = first_3 + puntini + last_3
print(concatena)
"""

"""
string = str(input("inserisci una frase: ")).upper()

new_string = string.replace("A", "a").replace("E", "e").replace("I", "i").replace("O", "o").replace("U", "u")
print(new_string)

"""