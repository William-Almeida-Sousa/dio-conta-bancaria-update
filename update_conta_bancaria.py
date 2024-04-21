from datetime import datetime
import os
import re

agencia = 237
contas = "0"
logado = False
saldo = 0
limite = 500
extrato_deposito = []
extrato_saque = []
numero_saques = 0
LIMITE_SAQUES = 3
deposito_valor = 0
saque_valor = 0
formulario = []
login = []
total = 0
user = ""

def criar_user():
   global formulario
   global login
   global contas
   global user
   global cpf
   global data_nascimento


   user = (input("Entre com seu nome de login (Apenas Letras):  "))
   user.lower()

   while not (re.search(r'[a-z]', user)):  
    user = input("Use como base os critérios informado: ")
    

   for x in login:
      if user in x:
        print("Nome já utilizado")
        input()
        return
  
    
   try:
    cpf = (input("Entre com o seu CPF(Apenas números):  "))
   except ValueError:
      print("Informação inválida!")
      input()
      return
   
   while True:
      if len(cpf) == 11:
         break
      else:
         print("CPF inválido!")
         input()
         return
      
    
   for x in login:
      if cpf in x:
        print("Usuário já cadastrado")
        input()
        return

   formulario.append(user)
   formulario.append(cpf)
   contas = int(contas) + 1
   formulario.append(agencia)
   formulario.append(str(contas).zfill(4)) 
   
  
   data_nascimento = input("Entre com o sua data de nascimento(Apenas 4 digitos):  ")

   if len(data_nascimento) == 8:
      data = datetime.strptime(data_nascimento, '%d%m%Y')
      data_nascimento = data.strftime('%d-%m-%Y')
      formulario.append(data_nascimento)
   else:
      print("Data inválida")
      input()
      return


   formulario.append(input("Entre com o seu endereço:  "))

   login.append(formulario)
   formulario = []
   print(login)
   input()

   os.system("cls")

def acesso():
   global user
   global logado
   global total
   global login
   
   user = input("Digite seu login:  ")
      
   for x in login:
      if user in x:
        logado = True
   
   if logado == False:
      print("Usuário não identificado")
      input()

   os.system("cls")

def deposito():
    global deposito_valor
    global saldo
    global extrato_deposito
    
    deposito_valor = int(input("Qual o valor do depósito?  Valor:  "))

    if deposito_valor > 0:
      print(f"Depósito realizado no valor de R${deposito_valor:,.2f}.")
      input()
      saldo += deposito_valor
      extrato_deposito.append(deposito_valor)
      deposito_valor = 0


    else:
      print("Valor inválido. Voltando para o menu principal.")
      input()

    os.system("cls")  
    #return saldo, deposito_valor, extrato_deposito
            
def saque():
      global saque_valor
      global numero_saques
      global saldo
      global extrato_saque
      
      saque_valor = int(input("Qual o valor do saque?  Valor:  "))

      if numero_saques == LIMITE_SAQUES:
        print("Número de Saques Diário Chegaram ao Limite! Disponível: 3 Saques Por Dia.")
        input()

      elif saque_valor > 500:
        print("Limite Máximo Diário São de 500 Reais!")
        input()

      elif saque_valor > 0 and saldo >= saque_valor and saque_valor <= 500 and numero_saques < 3:
        print(f"Saque realizado no valor de R${saque_valor:,.2f}.")
        input()
        saldo -= saque_valor
        numero_saques += 1
        extrato_saque.append(saque_valor)
        saque_valor = 0

      else:
        print("Valor inválido ou saldo insuficiente. Voltando para o menu principal.")
        input()

      os.system("cls")
      #return saque_valor, numero_saques, saldo, extrato_saque

def extrato():
      global extrato_deposito
      global extrato_saque
      global numero_saques
      global saldo
            
      print("Estamos Gerando o Seu Extrato Bancário")
      input("Tecle Para Continuar")
            


      print (
                  f"""

            ############### EXTRATO ###############

            Depósitos Realizados

            {extrato_deposito}

            Saques Realizados

            {extrato_saque}

            Número de Saques = {numero_saques}
            TOTAL = R${saldo:,.2f}

            ####################################
            => """
            )
      input()    
      
      os.system("cls")
      #return extrato_deposito, extrato_saque, numero_saques, saldo

while logado == False:

    print( """

      ############### MENU ###############

      [1] Criar Cadastro
      [2] Acessar Conta
      [0] Finalizar

      ####################################

      

                  Obrigado por uar nosso sistema!!!
    => """
    )
    
    opcao_false = int(input("Escolha uma das opções:  "))
    os.system("cls")

    if opcao_false == 1:
       criar_user()

    elif opcao_false == 2:
       acesso()

    elif opcao_false == 0:
      break
  
    else:
      print("Opção inválida. Por favor escolha uma opção válida.")
      input()
      os.system("cls")


while logado == True:
  
  print(  """

      ############### MENU ###############

      [1] Depositar
      [2] Sacar
      [3] Extrato
      [0] Finalizar

      ####################################

      

                  Obrigado por uar nosso sistema!!!
    => """
    )

  opcao = int(input("Escolha uma das opções:  "))
  os.system("cls")

  if opcao == 1:
    deposito()

  elif opcao == 2:
    saque()

  elif opcao == 3:
    extrato()  
        
  elif opcao == 0:
    break
                  

  else:
    print("Opção inválida. Por favor escolha uma opção válida.")
    input()
    os.system("cls")