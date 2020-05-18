import math
import random
import  time
from datetime import date 
#import pygame
'''print ('Alo Mundo')
a = 3
b = 4
print(a+b)'''

''' == Exercício 2
nome =  input("Digite seu nome: \n")
print("É um prazer te conhecer, {}" .format(nome))'''

'''Exercício 3
n1 = int(input("Digite um número\n"))
n2 = int(input("Digite um número\n"))
s = n1+n2
print("A soma entre {} e {} é: {}" .format(n1,n2,s))'''

''' Exercício 4
n1 = int(input("Digite um número\n"))
print("Seu antecessor é {} e seu sucessor é {}" .format(n1-1,n1+1))'''

'''Exercício 5
n1 = int(input("Digite um número\n"))
print("Seu dobro é {}, seu triplo é {} e sua raíz é {:.2f}" .format(n1*2,n1*3, math.sqrt(n1)))'''

'''Exercício 6
nota1 = float(input("Informe a primeira nota do aluno:"))
nota2 = float(input("Informe a segunda nota do aluno:"))
media = (nota1 + nota2)/2
print("A média do aluno é: {:.2f}" .format(media))'''

'''Exercício 7
metro = float(input("Informe os metros desejados:\n"))
cm = metro * 100
mm = metro * 1000
print("{} metro(s) é(são) {:.3f} centímetro(s) e {:.3f} milímetro(s)" .format(metro,cm,mm))'''

'''Exercício 8
tabuada = float(input("Digite um número para ver sua tabuada:\n"))
res1 = tabuada * 1
res2 = tabuada * 2
res3 = tabuada * 3
res4 = tabuada * 4
res5 = tabuada * 5
res6 = tabuada * 6
res7 = tabuada * 7
res8 = tabuada * 8
res9 = tabuada * 9
res10 = tabuada * 10
print("========= ==========\n {} x {} = {} \n {} x {} = {} \n {} x {} = {} \n {} x {} = {}\n {} x {} = {}\n {} x {} = {} \n {} x {} = {} \n{} x {} = {} \n{} x {} = {}\n{} x {} = {}\n" .format(tabuada,1,res1,tabuada,2,res2, tabuada, 3,res3, tabuada,4,res4,tabuada,5,res5,tabuada,6,res6,tabuada,7,res7,tabuada,8,res8,tabuada,9,res9,tabuada,10,res10))'''

'''Exercício 10
real = float(input("Quanto você tem em real(is)?\nR$"))
dolar = real * 5.24
print("Sendo assim, você consegue comprar US${:.2f}" .format(dolar))'''

''' Exercício 11
larg = float(input("Largura da parede:\n"))
alt = float(input("Altura da parede:\n"))
area = larg*alt
print("àrea: {:.2f}m²" .format(area))
litros = area/2
print("Litros de tinta: {:.2f}l" .format(litros))'''

'''Exercício 12
prod = float(input("Informe o valor do produto: \nR$"))
promo = prod * 0.05
res = prod - promo
print("O produto que custava R${:.2f}, na promoção com desconto de 5%, vai custar R${:.2f}" .format(prod,res))'''

'''Exercício 13
sal = float(input("Infome o salário do funcionário: \nR$"))
promo = sal * 0.15
aum = sal + promo
print("O salário que era R${:.2f}, com o aumento de 15%, vai ser R${:.2f}" .format(sal,aum))'''

'''Exercício 14
temp = float(input("Informa a temperatura em C°: \n"))
f = (temp*(9/5)) + 32
print("A temperatura de {:.1f}C° corresponde a {:.1f}F°" .format(temp,f))'''

'''Exercício 15
dias = int(input("Quantos dias rodados no carro?\n"))
km = float(input("Quantos quilômetros rodados no carro?\n"))
p_dia = dias * 60
p_km = km * 0.15
p_res = p_dia + p_km
print("Você deve pagar: R${:.2f}" .format(p_res))'''

'''Módulos
ceil -> média
floor
trunc
pow
sqrt 
factorial
num = float(input("Informe um número"))
raiz = math.int(num)
print("{}" .format(raiz))
num2 = random.randint(1,10)
#print(num2)
#print(emoji.emojize("Olá mundo :sunglasses:", use_aliases=True))'''

'''Exercício 16
num = float(input("Informe o número float:\n"))
num2 = math.trunc(num)
print("A parte inteira é {}".format(num2))'''

'''Exercício 17
cat_a = float(input("informe o cateto adjascente:\n"))
cat_o = float(input("informe o cateto oposto:\n"))
hip = cat_a**2 + cat_o**2
hip2 = math.sqrt(hip) 
print("A hipotenusa é: {:.2f}" .format(hip2))'''

'''Exercício 18
ang = float(input("Informe o ângulo desejado:\n"))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print("Seno:{:.2f}\nCoseno: {:.2f}\nTangente: {:.2f}" .format(sen,cos,tan))'''

'''Exercício 19
al1 = str(input("Informe o nome do(a) aluno(a):\n"))
al2 = str(input("Informe o nome do(a) aluno(a):\n"))
al3 = str(input("Informe o nome do(a) aluno(a):\n"))
al4 = str(input("Informe o nome do(a) aluno(a):\n"))
lista = [al1,al2,al3,al4]
sorteio = random.shuffle(lista) #Embaralha toda a ordem
sorteio2 = random.choice(lista) #Aqui escolhe só um
print("O aluno escolhido é {}" .format(sorteio))'''

'''Exercício 20
pygame.init()
pygame.mixer.music.load('mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

'''Módulo 9
frase = 'hello man'
print(frase[3])
frase[3:13] Do 3 ao 12
frase[12:32:2] Pular de 2 em 2
frase[:5]
frase[3:]
frase[9::3]9 até o final pulando de 3 em 3
len(frase) Comprimento da frase
frase.count('o')Conta quantos o
frase.count('o',0,13)Conta quantos o do 0 ao 12
frase.find('deo')Mostra a posição 
'Curso' in frase
frase.replace('Python','Android') Substitui as palavras
frase.upper()Maiúscua
frase.lower()Minúsculo
frase.capitalize()Deixa a primeira maiúscula
frase.title()Deixa os inícios da palavra em maiúscula 
frase.strip()REmove espaços inúteis
frase.rstrip()REmove espaços inúteis da direita
frase.lstrip()REmove espaços inúteis da esquerda
frase.split()Separa várias listas novas
'-'.join(frase)Palvra-palavra-Palvra
dividido = frase.split()
print(dividido[0])'''

'''Exercício 22
nome = str(input("Informe o seu nome completo:\n")).strip()
m = nome.upper()
print(m)
m2 = nome.lower()
print(m2)
print("{}" .format(len(nome) - nome.count(' ')))
print("{}" .format(nome.find(' ')))'''

'''Exercício 23
num = int(input("Informe o número de 0 9999:\n"))
n = str(num)
print("Unidade:{}" .format(n[3]))
print("Dezena:{}" .format(n[2]))
print("Centena:{}" .format(n[1]))
print("Milhar: {}" .format(n[0]))'''

'''Exercício 24
cid = str(input("Informe a cidade desejada:")).strip() #strip retira os espaços
print(cid[:5].upper() == 'SANTO' )'''

'''Exercício 25
nome = str(input("Informe seu nome:\n")).strip()
print("Seu nome tem Silva? {}" .format('SILVA' in nome.upper()))'''

'''Exercício 26
nome = str(input("Informe o nome:\n")).upper()
print("Seu nome tem {} letras A's" .format(nome.count('A')))
print("A letra A foi encontrada primeiramente na posição {}" .format(nome.find('A')+1))
print("A última letra A está na posição {}" .format(nome.rfind('A')+1))'''

'''Exercício 27
nome = str(input("Informe o seu nome:\n")).strip()
n = nome.split() 
print("Seu primeiro nome é:{}" .format(n[0]))
print("Seu último nome é {}" .format(n[len(n)-1]))'''

'''Módulo 10 Part 1
== Condição == 
if fmrkmrefmkfer:
    bloco
else:
    bloco
== Condição Simplificada ==
print('Carro novo'iftempo<=3else'carro velho')'''

'''Exercício 28
print("hummm... Estou pensando em um número de 0 a 5!!")
num = int(input("Qual o número que você acha que eu pensei:\n"))
print("PROCESSANDO...")
time.sleep(1)
if num == 4:
    print("Parabéns, você venceu!")
elif num > 5:
    print("Número errado, por favor, tente de novo!")
    num = int(input("Qual o número que você acha que eu pensei:\n"))
if num == 4:
    print("Parabéns, você venceu!")
else:
    print("Hehehehe, você perdeu,a resposta era {}!" .format(num))
print("==Fim==")'''

'''Exercício 30
print("== Sistema de trânsito ==")
vel = float(input("Informe a velocidade do seu veículo:\n"))
if vel > 80:
    multa = vel - 80
    if multa > 1:
        multa_valor = multa * 7
        print("Você excedeu a velocidade e infelizmente foi multado!!")
        print("Sua multa é no valor de R${:.2f}" .format(multa_valor))
    else:
        print("Por sorte, você ficou na margem de erro de 1 km!!")
        print("Tenha mais cuidado")
else:
    print("Tudo bem, você está no limite de velocidade aceitável de 80km!!:)")
print(" === Beba com moderação! ===")'''

'''Exercício 30
num = int(input("Me diga um número qualquer:\n"))
if num % 2 == 0:
    print("Número par!")
else:
    print("Número ímpar!")'''

'''Exercício 31
print("=== Companhia Guanabara ===\n")
viagem = float(input("Quantos km's são sua viagem?\n"))
if viagem <= 200:
    print("Viagens até 200 km's, cobramos R$0,50 por km!")
    valor = viagem * 0.50
    print("Logo, o valor de sua viagem é de R${:.2f}" .format(valor))
else:
    print("Viagens acima de 200 km's, cobramos R$0,45 por km!")
    valor = viagem * 0.45
    print("Logo, o valor de sua viagem é de R${:.2f}" .format(valor))
print("Boa Viagem!")'''

'''Exercício 32
ano = int(input("Informe o ano que você gostaria de ser analisado. Caso seja atual, digite 0:\n"))
if ano <= 0:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("O ano atual é BISSEXTO!!")
    else:
        print("O ano atual não é BISSEXTO!")
elif ano > 0 and ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO!!" .format(ano))
else:
    print("O ano {} não é BISSEXTO!" .format(ano))'''

'''Exercício 32
num1 = float(input("Primeiro número:\n"))
num2 = float(input("Segundo número:\n"))
num3 = float(input("Terceiro número:\n"))

if num1 > num2 and num1 > num3:
    print("O número {} é o maior!" .format(num1))
elif num2 > num1 and num2 > num3:
    print("O número {} é o maior!" .format(num2))
elif num3 > num1 and num3 > num2:
    print("O número {} é o maior!" .format(num3))
else:
    print("Os números são iguais!")

if num1 < num2 and num1 < num3:
    print("O número {} é o menor!" .format(num1))
elif num2 < num1 and num2 < num3:
    print("O número {} é o menor!" .format(num2))
elif num3 < num1 and num3 < num2:
    print("O número {} é o menor!" .format(num3))'''

'''Exercício 33
print("=== Empresa Aplle ===\n")
sal = float(input("Informe o seu sálario:\nR$"))
if sal <= 1250.00:
    val_sal = sal * 0.1 + sal
    print("Seu aumento foi de 10%. Logo, seu salário passou para R${:.2f}" .format(val_sal))
else:
    val_sal = sal * 0.15 + sal
    print("Seu aumento foi de 15%. Logo, seu salário passou para R${:.2f}" .format(val_sal))'''

'''Exercício 35
reta1 = float(input("Informe o valor da reta 1:\n"))
reta2 = float(input("Informe o valor da reta 2:\n"))
reta3 = float(input("Informe o valor da reta 3:\n"))

reta_t1 = reta1 + reta2
reta_t2 = reta1 + reta3
reta_t3 = reta3 + reta2

if reta_t1 > reta3 or reta_t2 > reta2 or reta_t3 > reta1:
    print("Pode - se formar um triângulo à partir destas retas!")
    print("    /\ ")
    print(" {:.0f}/  \{:.0f} " .format(reta1,reta2))
    print("  /____\    "     )
    print("   {}   ".format(reta3))
else:
    print("Não pode - se formar um triângulo à partir destas retas!")  '''

'''Módulo 11
#\033[0:33:32m
#print('\033[32;31mOlá mundo!') #Vermelho
#print('\033[1;31;43mOlá mundo!\033[m') #Fundo Amarelo e letra em negrito e fecha no final
#print('\033[4;31;43mOlá mundo!\033[m') #Fundo Amarelo e letra sublinhada e fecha no final
#print('\033[7;30;37mOlá mundo!\033[m') #Invertendo --- Fundo branco, letra preta ---
a = 4
b = 5
print('Os valores são\033[32m{} \033[31m{}' .format(a,b)) #Trocando cores de variáveis
print('{}{}{}!!!' .format('\033[4;34m',a,'\033[m')) #Definindo cores nas chaves'''

'''Exercício 36
print("=== Empréstimo ===\n")
valor_casa = float(input("Informe o valor da casa:\nR$"))
sal = float(input("Informe sua renda mensal:\nR$"))
anos = float(input("Em quantos anos você pretende pagar o empréstimo:\n"))
meses = anos * 12
prest = valor_casa/meses
sal_pagar = sal * 0.30

if prest <= sal_pagar:
    print("Seu empréstimo foi aceito!!")
    print("você irá pagar em {:.2f} meses e sua prestação mensal será RS{:.2f}" .format(meses, prest))
else: 
    print("A prestação excedeu os 30%"" de sua renda, infelizmente seu empréstimo foi negado!")'''

'''Exercício 37
num = int(input("informe um número inteiro qualquer:\n"))
print("[1] Converter para BINÁRIO")
print("[2] Converter para OCTAL")
print("[3] Converter para HEXADECIMAL")
opcao = int(input("Sua opção:"))
while (opcao > 3 or opcao < 0):
    print("Número Invalido!!\nTente Novamente:)")
    opcao = int(input("Sua opção:"))
if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}" .format(num,bin(num)))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}" .format(num,oct(num)))
else:
    print("{} convertido para HEXADECIMAL é igual a {}" .format(num,hex(num)))'''

'''Exercício 39
atual = date.today().year
ano = int(input("Em que ano você nasceu?\n"))
idade = atual - ano
print("Quem nasceu em {} tem {} anos em {}!" .format(ano, idade, atual))

if idade == 18:
    print("Você está na hora de se alistar imediatamente!!")
elif idade < 18:
    saldo = 18 - idade
    print("Você possui {} anos e não está na hora de você se alistar!!" .format(idade))
    print("Ainda falta(m) {} ano(s) para você se alistar!" .format(saldo))
elif idade > 18:
    saldo = idade - 18
    print("Você possui {} anos e já passou da hora de você se alistar!!" .format(idade))
    print("Você já passou {} ano(s) de atraso" .format(saldo))'''

'''Exercício 41
atual = date.today().year
nasc = int(input(("Em qual ano você nasceu?\n")))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}!" .format(nasc, idade, atual))

if idade <= 9:
    print("Você possui {} anos e não está na categoria MIRIM!!" .format(idade))
elif idade > 9 and idade <= 14:
    print("Você possui {} anos e não está na categoria INFANTIL!!" .format(idade))
elif idade > 14 and idade <= 19:
    print("Você possui {} anos e não está na categoria JUNIOR!!" .format(idade))
elif idade > 19 and idade <= 25:
    print("Você possui {} anos e não está na categoria SÊNIOR!!" .format(idade))
else:
    print("Você possui {} anos e não está na categoria MASTER!!" .format(idade))'''

'''Exercício 42
reta1 = float(input("Informe o valor da reta 1:\n"))
reta2 = float(input("Informe o valor da reta 2:\n"))
reta3 = float(input("Informe o valor da reta 3:\n"))

reta_t1 = reta1 + reta2
reta_t2 = reta1 + reta3
reta_t3 = reta3 + reta2

if reta_t1 > reta3 and reta_t2 > reta2 and reta_t3 > reta1:
    if reta1 == reta2 == reta3:
        print("Pode - se formar um triângulo à partir destas retas!")
        print("O triângulo é equilátero!!")
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1 :
        print("Pode - se formar um triângulo à partir destas retas!")
        print("O triângulo é isósceles!!")
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1 :
        print("Pode - se formar um triângulo à partir destas retas!")
        print("O triângulo é escaleno!!")
else:
    print("Não pode - se formar um triângulo à partir destas retas!")  '''
    
'''Exercício 43
peso = float(input("Informe seu peso:\n(Kg)"))
altura = float(input("Informe sua altura:\n(m)"))

imc = peso/(altura*altura)

if imc < 18.5:
    print("Seu IMC é igual a {}. Você está abaixo do peso!" .format(imc))
elif imc >= 18.5 and imc < 25:
    print("Seu IMC é igual a {}. Você está no peso ideal!" .format(imc))
elif imc >= 25 and  imc < 30:
    print("Seu IMC é igual a {}. Você está com sobrepeso!" .format(imc))
elif imc >= 30 and imc <= 40:
    print("Seu IMC é igual a {}. Você está em obesidade!" .format(imc))
else:
    print("Seu IMC é igual a {}. Você está em obesidade mórbida!" .format(imc))
#pot = n2**2 #potência ========= {:>, <:, :=^,} ========== poder do print
#resto = n2%2 #resto
#div_inteira = n2//2'''

'''Exercício 44
print(" === LOJA TEM DE TUDO ===")
compras = float(input("Preço das compras:\nR$"))
print("[1] à vista dinheiro/cheque")
print("[2] à vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
op = int(input("Qual a opção escolhida:\n"))

if op == 1:
    desc = compras - compras * 0.1
    print("Você comprará a vista! Você terá 10%" "de desconto  em sua compra!")
    print("O valor de sua compra será de {:.2f}" .format(desc))
elif op == 2:
    desc = compras - compras * 0.05
    print("Você comprará a vista no cartão! Você terá 5%" "de desconto  em sua compra!")
    print("O valor de sua compra será de {:.2f}" .format(desc))
elif op == 3:
    parc_compra = compras/2
    print("Você comprará de 2x no cartão! Sua compra sairá pelo preço normal!")
    print("O valor de sua compra será de 2x de {:.2f}" .format(parc_compra))
elif op == 4:
    parcelas = int(input("Em quantas parcelas?\n"))
    total = compras + (compras*0.2)
    parc_compra = total / parcelas
    print("O valor de sua compra será de {}x de {:.2f} com 0.2 de juros" .format(parcelas,parc_compra))'''

'''Exercício 45
print("Sua opção:")
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
jogada = int(input("Informe sua escolha:\n"))
jogada_p = 0
print("JO")
print("KEN")
print("PO!!")
if jogada == jogada_p:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Computador jogou pedra!")
    print("Você jogou pedra!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print("Jogo Empate!")
elif jogada == 1:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Computador jogou pedra!")
    print("Você jogou papel!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print("Você venceu!!")
elif jogada == 2:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Computador jogou pedra!")
    print("Você jogou tesoura!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print("Você perdeu!!")'''

''' Módulo 13
for c in range(1,10):
    passo
pega
for c in range(0,3):
    if moeda:
        pega
    passo
    pula
passo
pega
for c in range(1,7): #Quiser descendente é: range(7,0,-1)
    print(c)
print("FIM")
num = int(input("Informe"))
for c in range(0,num+1):
    print(c)
print("FIM")
ini = int(input("inicio"))
fim = int(input("Fim"))
passo = int(input("passo"))
for c in range(ini, fim+1, passo):
    print(c)
s = 0
for c in range(0,10):
    num = int(input("INforme um valor:"))
    s += num
print("o somatório dos valores foi {}" .format(s))'''

'''Exercício 46
for c in range(10,0,-1):
    print(c)
    time.sleep(1)
print("BUM BUM POW")'''

'''Exercício 47
for c in range(0,52,2):
    print(".", end= ' ')
    print(c, end = ' ')'''

'''Exercício 48
som = 0
c2 = 0
for c in range(1,500+1, 2):
    if c % 3 ==0:
        c2 = c2 + 1 
        som = som + c
print("São {} números múltiplos de 3 e a soma deles é: {}" .format(c2, som))'''

'''Exercício 49
tab = int(input("Informe o número desejado:\n"))

for c in range(1,10+1):
    print("{} X {} = {}" .format(tab,c,tab*c))'''

'''Exercício 50
print("Informe os 6 números:")

par = 0
soma = 0
impar = 0
for c in range(0,6):
    num = int(input(""))
    if num % 2 == 0:
        par = par + 1
        soma = soma + num
    else: 
        impar = impar + 1
print("São {} pares e a soma deles é: {}" .format(par, soma))
print("Foram {} ímpares e foram descartados." .format(impar))'''

'''Exercício 51
p_termo = int(input("Informe o primeiro termo da PA:\n"))
r = int(input("Informe a razão:\n"))
decimo = p_termo + (10-1) * r
for c in range(p_termo,decimo,r):
    print("{}".format(c), end=" -> " )
print("ACABOU")'''

'''Exercício 52
num = int(input("Informe um número:"))
count = 0
for c in range(1,num+1):
    if num % c == 0:
        count = count + 1
print("O número {} foi dividido {} vezes" .format(num, count))
if count == 2:
    print("Ele é primo!")
else:
    print("Não é primo!")'''

''' Exercício 53
frase = str(input("Informe a frase desejada:\n")).strip().upper() Divide os blocos e coloca em maiúsculo
palavras = frase.split()Divide em palavras
junto = ''.join(palavras)Junta as palavras
inverso = '' inicializando a variável que pegará o inverso
for letra in range(len(junto) -1, -1, -1): da última letra até a primeira, pulando de -1 em -1
    inverso += junto[letra]
print("O contrário é {}" .format(inverso))
if inverso == junto:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")'''

'''Exercício 54
idade = 0
atual = date.today().year 
count1 = 0
count2 = 0
for vezes in range(1, 7 +1):
    ano = int(input("Informe o {}° ano de nascimento:\n" .format(vezes)))
    idade = atual - ano
    if idade >= 18:
        count1 += 1
    else:
        count2 += 1
print("Há nesse grupo {} maiores de idade" .format(count1))
print("Há nesse grupo {} menores de idade" .format(count2))'''

'''Exercício 56
for vezes in range(1,6):
    peso = float(input("Informe o peso da {}ª pessoa:" .format(vezes)))
    if vezes == 1:
        maior = vezes
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso foi {}kg" .format(maior))
print("O menor peso foi {}kg" .format(menor))'''

'''Exercício 56
comp = ''
representa = ''
count = 0
soma = 0
for vezes in range(1,4+1):
    print("=== {}ª Pessoa ===".format(vezes))
    if vezes == 1:
        maior = vezes
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    comp = sexo
    if comp == 'M':
        if idade > maior:
            maior = idade
            representa = nome
    if comp == 'F':
        if idade < 20:
            count += 1
    soma += idade
media = soma / 4

print("A média de idade do grupo é {:.2f}" .format(media))
print("O homem mais velho tem {} anos e seu nome é {}" .format(maior, representa))
print("{} mulhere(s) tem menos que 20 anos!".format(count))'''

'''Módulo 14
==== While ====
enquanto não maçã
    passo 
pega
while not maçã
    passo
pega
while not maçã:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega maçã
c = 1
c = 1
while c < 10:   
    print(c)
    c += 1
print("FIM")
r = 'S'
while r == 'S':
    n = int(input("digite um número:\n"))
    r = str(input("Quer continuar?[S/N]")).upper()'''

''' Exercício 57 
sexo = str(input("Por favor, informe seu sexo: [M/F]\n")).upper()
while sexo != 'M' and sexo != 'F':
    print("Tecla inválida!")
    sexo = str(input("Por favor, informe seu sexo: [M/F]\n")).upper()
print("Valor Correto, sexo do tipo {} registrado!" .format(sexo))'''

'''Exercício 58
print("Sou seu computador...")
print("Será que você consegue adivinhar qual foi?")
hip = int(input("Qual é o seu palpite?"))

while hip != 8:
    if hip < 8:
        print("Mais...Tente mais uma vez.")
        hip = int(input("Qual é o seu plano?"))
    else:
        print("Menos...Tente mais uma vez.")
        hip = int(input("Qual é o seu plano?"))
print("Parabéns, você acertou!! Pensei em {}!" .format(hip))'''

'''Exercício 59
op = 0
while op != 5:
    print("\n")
    primeiro = float(input("Primeiro Valor:"))
    segundo = float(input("Segundo Valor:"))

    print("   [1] somar")
    print("   [2] multiplicar")
    print("   [3] maior")
    print("   [4] novos números")
    print("   [5] sair do programa")

    op = int(input(" >>> Qual é sua opção?"))
    if op == 1:
        soma = primeiro + segundo
        print("O resultado é {} + {} = {}" .format(primeiro, segundo, soma))
    if op == 2:
        mult = primeiro * segundo
        print("O resultado é {} x {} = {}" .format(primeiro, segundo, soma))
    if op == 3:
        if primeiro > segundo:
            print("O {} é maior" .format(primeiro))
        else:
            print("O {} é maior" .format(segundo))

print("===FIM===")'''

'''Exercício 60
fat = int(input("Digite um número para conseguirmos seu fatorial:"))
var = fat
mult = 1 
while fat != 0:
    mult = mult * fat
    fat = fat - 1

print("Calculando {}! = {}" .format(var,mult))'''

'''Exercício 61 e 62
print("Gerador de PA")
print("================")
a1 = int(input("Primeiro termo:"))
r =  int(input("Razão da PA:"))
count = 10

print("{} ->" .format(a1), end='')
while count > 0:
    a1 += r
    print("{} -> " .format(a1), end='')
    count -= 1
    if count == 1:
        print("PAUSA")
        count = int(input("Você quer mostrar mais termos?"))
        if count > 0:
            count += 1'''

'''Exercício 63
t1 = 0
t2 = 1
t3 = 0
num = int(input("Quantos termos você quer mostrar?\n"))
#print("0-> 1-> ", end='')
while num > 0:
    t3 = t1 + t2
    print("{} -> " .format(t3), end='')
    t1=t2
    t2=t3
    num -= 1
print("FIM")'''

'''Exercício 64
count = 0
soma = 0
num = 0
while num != 999:
    num = int(input("Digite um número[999 para parar]:\n"))
    count += 1
    soma += num

print("Você digitou {} número(s) e a soma entre eles foi {}." .format(count, soma))'''

'''Exercício 65
letra =''
count = 1
maior = 0 
num = int(input("Digite um número: "))
letra = str(input("Quer continuar?[S/N]")).upper()
menor = num
soma = num
while letra != 'N':
    num = int(input("Digite um número: "))
    letra = str(input("Quer continuar?[S/N]")).upper()
    count += 1
    soma += num
    if num > maior:
        maior = num
    if  num < menor:
        menor = num
media = soma / count

print("Você digitou {} número(s) e a média foi {:.2f}" .format(count,media))
print("O maior valor foi {} e o menor foi {}" .format(maior,menor))'''

'''Módulo 15
while verdadeiro:
    if rocha:
        anda
    if vazio:
        pula
    if moeda:
        pega
    if troféu:
        pula
        break
pega
'''

'''Exercício 66
num = soma = count = 0

while True:
    num = int(input("Digite um número: [999 para sair]"))
    if num == 999:
        break
    count += 1
    soma += num
print("Foram digitados {} números e a soma deles foi {}" .format(count,soma))'''

'''Exercício 67
tab = mult = 0
num = 1
print("=============================================")
tab = int(input("Quer ver a tabuada de qual valor:"))
print("=============================================")
while num < 12:
    if tab < 0:
        print("PROGRAMA DE TABUADA ENCERRADO! VOLTE SEMPRE!")
        break
    mult = tab * num 
    print("{} x {} = {}" .format(tab,num,mult))
    num += 1
    if num == 11:
        num = 1
        print("=============================================")
        tab = int(input("Quer ver a tabuada de qual valor:"))
        print("=============================================")'''

'''Exercício 68
num = val = 0
count = count2 = 0
decisao = ''
while num < 3:
    print("======================")
    print("VAMOS JOGAR PAR OU IMPAR")
    print("======================")
    val_usu = int(input("Diga um valor:"))
    decisao_usu = str(input("Par ou Ímpar:[P/I]")).upper()
    val_comp = random.randint(1,100)
    soma = val_usu + val_comp
    if decisao_usu == 'P':
        if soma % 2 == 0:
            count += 1
            print("Você jogou {} e a máquina {}. Total de {} deu PAR." .format(val_usu, val_comp, soma))
            print("Você venceu!")
        else:
            count2 += 1
            print("Você jogou {} e a máquina {}. Total de {} deu IMPAR." .format(val_usu, val_comp, soma))
            print("Máquina venceu!")
    if decisao_usu == 'I':
        if soma % 2 != 0:
            count += 1
            print("Você jogou {} e a máquina {}. Total de {} deu IMPAR." .format(val_usu, val_comp, soma))
            print("Você venceu!")
        else:
            count2 += 1
            print("Você jogou {} e a máquina {}. Total de {} deu PAR." .format(val_usu, val_comp, soma))
            print("Máquina venceu!")
    if count == 2 or count == 3:
        print("VOCÊ VENCEU!!")
        print("===================")
        print("GAME OVER. VOCÊ VENCEU {} vezes" .format(count))
        break
    if count2 == 2 or count2 == 3:
        print("===================")
        print("MÁQUINA VENCEU!!")
        print("===================")
        print("GAME OVER. MÁQUINA VENCEU {} vezes" .format(count2))
        break'''


'''Exercício 69
decisao = 'S'
sexo = ''
count = count_m = count3 = 0
while decisao == 'S':
    print("======================")
    print("CADASTRE UMA PESSOA")
    print("======================")
    idade = int(input("Idade:"))
    sexo = str(input("Sexo:")).upper()
    if idade > 18:
        count += 1
    if sexo == 'M':
        count_m += 1
    if sexo == 'F':
        if idade < 20:
            count3 += 1
    print("=========================")
    decisao = str(input("Quer continuar? [S/N]")).upper()
    if decisao == 'N':
        break 

print("Total de pessoas com mais de 18 anos: {}" .format(count))
print("Ao todo temos {} homem(s) cadastrado(s)" .format(count_m))
print("Temos {} mulheres com menos de 20 anos" .format(count3))'''

'''Exercício 70
count = soma = menor_preco = 0
print("======================")
print("LOJA SUPER BARATÃO")
print("======================")
nome_produto = str(input("Nome do produto: ")).upper()
string_count = nome_produto
preco = float(input("Preço: R$"))
menor_preco = preco
print("=========================")
decisao = str(input("Quer continuar? [S/N]")).upper()
while decisao == 'S':
    print("======================")
    print("LOJA SUPER BARATÃO")
    print("======================")
    nome_produto = str(input("Nome do produto: ")).upper()
    preco = float(input("Preço: R$"))
    soma += preco
    if preco > 1000:
        count += 1
    if preco < menor_preco:
        menor_preco = preco
        string_count = nome_produto
    print("=========================")
    decisao = str(input("Quer continuar? [S/N]")).upper()
    if decisao == 'N':
        break 

print("Total de compra foi: R${:.2f}" .format(soma))
print("Temos {} produto custando mais que R$1000.00" .format(count))
print("O produto mais barato foi {} que custa R${:.2f}" .format(string_count,menor_preco))'''

'''Exercício 71
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0

print("=====================")
print("BANCO RUANN")
print("=====================")
valor= int(input("Qual valor você deseja sacar? "))

while valor >= 50:
    ced50 += 1
    valor -= 50 
    if valor < 50:
        print("Total de {} cédulas de R$50".format(ced50))
while valor >= 20:
    ced20 += 1
    valor -= 20 
    if valor < 20:
        print("Total de {} cédulas de R$20".format(ced20))
while valor >= 10:
    ced10 += 1
    valor -= 10 
    if valor < 10:
        print("Total de {} cédulas de R$10".format(ced10))
while valor >= 1:
    ced1 += 1
    valor -= 1 
    if valor < 1:
        print("Total de {} cédulas de R$1".format(ced1))'''


