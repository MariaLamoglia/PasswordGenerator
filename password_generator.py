import random # CONTÉM FUNÇÕES PARA GERAR NÚMEROS E FAZER ESCOLHAS ALEATÓRIAS
import string # COLEÇÃO DE CONSTANTES DE STRING ÚTEIS (LETRAS, NÚMEROS E SÍMBOLOS)
import secrets # MÓDULO MAIS SEGURO PARA GERAÇÃO DE ALEATORIEDADE CRIPTOGRÁFICA

def generate_secure_password(length = 12):
    if length < 8: 
        print("O comprimento da senha deve ser de pelo menos 8 caracteres!")
        return None
    
    # GARANTINDO PELO MENOS 1 CARACTERE DE CADA TIPO
    password_list = [
        secrets.choice(string.ascii_lowercase), # RECEBE PELO MENOS 1 LETRA MINÚSCULA
        secrets.choice(string.ascii_uppercase), # RECEBE PELO MENOS 1 LETRA MAIÚSCULA
        secrets.choice(string.digits), # RECEBE PELO MENOS 1 DÍGITO DE 0 A 9
        secrets.choice(string.punctuation) # RECEBE PELO MENOS 1 DOS CARACTERES DE PONTUAÇÃO MAIS COMUNS
    ]

    # PREENCHENDO O RESTO DA SENHA COM UMA SELEÇÃO ALEATÓRIA DE TODOS OS CARACTERES
    all_chars = string.ascii_letters + string.digits + string.punctuation

    remaining_length = length - len(password_list) # CALCULA QUANTOS FALTAM
    for _ in range(remaining_length):
        password_list.append(secrets.choice(all_chars)) # CADA VOLTA DO LAÇO, UM NOVO CARACTERE ALEATÓRIO É ADD A LISTA, GARANTINDO QUE A SENHA FINAL TENHA O COMPRIMENTO EXATO QUE O USUÁRIO SOLICITOU

    # EMBARALHANDO A LISTA PARA GARANTIR QUE OS CARACTERES OBRIGATÓRIOS NÃO FIQUEM NO INÍCIO
    random.shuffle(password_list)

    # JUNTANDO A LISTA DE CARACTERES EM UMA STRING FINAL
    return "".join(password_list)

# INTERAÇÃO COM O USUÁRIO
try:
    user_choice_str = input("Quantos dígitos na senha? (padrão: 12) ")

    # PERMITE QUE O USUÁRIO PRESSIONE 'ENTER' PARA USAR O VALOR PARÃO
    if not user_choice_str:
        user_choice = 12
    else: 
        user_choice = int(user_choice_str) # CONVERTE A STRING PARA UM NÚMERO INTEIRO

    # VALIDAÇÃO DO INTERVALO DE TAMANHO
    if not (8 <= user_choice <= 128):
        print("Tamanho inválido! Por favor, escolha um número entre 8 e 128.")
    else: 
        # GERAÇÃO E IMPRESSÃO DA SENHA
        generate_password = generate_secure_password(length = user_choice)
        if generate_password:
            print(f"Senha gerada: \n{generate_password}") # 'f' ANTES DA STRING INDICA QUE É UMA "f-string", PERMITINDO COLOCAR VARIÁVEIS DIRETAMENTE DENTRO DELA USANDO '{}'

except ValueError:
    # BLOCO EXECUTADO SE 'int(user_choice_str)' FALHAR
    print("Entrada inválida! Por favor, digite um número.")
