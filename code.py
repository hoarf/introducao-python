print(2+2)
print(9/2)
print(9/2.5)
print(1*7)
print(-5-(-2))
print(10>9)
print(15<12)
print(15<=15)

# Uso de variáveis e memória.

my_name = "Alan"
my_age = 31
my_height = 1.79 # metros
my_weight = 80 # kilos
my_eyes = "Castanhos"
my_hair = "Escuros"

print()
print(my_name)
print(my_height)
print(my_hair)
print(my_weight)

# Como lidar com strings.
# %d : use com digitos
# %s : use com strings
# %r : use quando você quer só uma _representação_ do valor
print("Vamos falar sobre %s" % my_name)
print("Eu tenho %d metros de altura" % my_height)
print("Ele pesa %d kilos" % my_weight)
print("Pra falar a verdade isso nem é muito pesado")
print("Ele tem os olhos %s e os cabelos %s" % (my_eyes, my_hair))

# Essa linha é complicada
print("Se eu somar %d, %d, e %d isso da %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

# Fazendo perguntas ao usuário.
user_age = input("Quantos anos você tem ")
user_weight = input("Quanto você pesa ")
user_height = input("Quanto você mede ")
print("Então você tem %r anos, pesa %r kilos e mede %r metros!" % (user_age, user_weight, user_height))

* [ ] Exercício: Fazer um programa que pergunte o peso e a altura do usuário e devolva o Índice de Massa Corporál (SE VIREM)
