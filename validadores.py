# Alfabetos utilizados
sigma = set("abcdefghijklmnopqrstuvwxyz")
gamma = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
n = set("0123456789")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Máscaras de Validação
def validar_nome(cadeia):
    if cadeia.count(" ") != 1:
        return False

    nome, sobrenome = cadeia.split(" ")

    if len(nome) < 2 or len(sobrenome) < 2: 
        return False

    if nome[0] not in gamma or sobrenome[0] not in gamma:
        return False

    for letra in nome[1:]:
        if letra not in sigma:
            return False
    for letra in sobrenome[1:]:
            if letra not in sigma:
                return False    

    return True
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def validar_email(cadeia):
    if cadeia.count("@") != 1 or not cadeia.endswith(".br"):
        return False

    usuario, email = cadeia.split("@")
    dominio = email[:-3]

    if len(usuario) == 0 or len(dominio) == 0:
        return False 

    for letra in usuario:
        if letra not in sigma:
            return False
    for letra in dominio:
        if letra not in sigma:
            return False

    return True
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def validar_senha(cadeia):
    if len(cadeia) != 8:
        return False

    tem_gamma = False
    tem_numero = False 

    for letra in cadeia:
        if letra in gamma:
            tem_gamma = True 
        elif letra in n:
            tem_numero = True
        elif letra in sigma:
            pass 
        else:
            return False

    validacao = tem_gamma and tem_numero

    return validacao
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def validar_cpf(cadeia):
    #xxx.xxx.xxx-xx são 14 caracteres
    if len(cadeia) != 14:
        return False 

    for carac in range(14):
        if carac == 3 or carac == 7:
            if cadeia[carac] != ".":
                return False 
        elif carac == 11:
            if cadeia[carac] != "-":
                return False
        elif cadeia[carac] not in n:
            return False

    return True
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def validar_telefone(cadeia):
    # Formato: (xx) 9xxxx-xxxx são 15 caracteres
    if len(cadeia) == 15:
        if (cadeia[0] != '(' or 
            cadeia[3] != ')' or 
            cadeia[4] != ' ' or
            cadeia[5] != '9' or 
            cadeia[10] != '-'):
            
            return False

        digitos_primeiro_formato = [1,2,6,7,8,9,11,12,13,14]
        for d in digitos_primeiro_formato:
            if cadeia[d] not in n:
                return False
    
        return True     

    #Formato: (xx) 9xxxxxxxx são 14 caracteres     
    elif len(cadeia) == 14:
        if (cadeia[0] != '(' or 
            cadeia[3] != ')' or 
            cadeia[4] != ' ' or
            cadeia[5] != '9'):

            return False   

        digitos_segundo_formato = [1,2,6,7,8,9,10,11,12,13]
        for d in digitos_segundo_formato:
            if cadeia[d] not in n:
                return False 

        return True

    #Formato: xx 9xxxxxxxx são 12 caracteres
    elif len(cadeia) == 12:
        if (cadeia[2] != ' ' or 
            cadeia[3] != '9'):

            return False

        digitos_terceiro_formato = [0,1,4,5,6,7,8,9,10,11]
        for d in digitos_terceiro_formato:
            if cadeia[d] not in n:
                return False 

        return True

    return False
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Função de Execução da Validação
def executar_validacao(tipo_validacao, funcao_validadora, exemplo):
    print(f'\nValidação de {tipo_validacao}')
    print(f'Exemplo de formato aceito: {exemplo}')

    entrada = input(f"Digite o {tipo_validacao}: ").strip()

    if funcao_validadora(entrada):
        print(f"\nA cadeia '{entrada}' é válida para o campo {tipo_validacao}!")
    else:
        print(f"\nA cadeia '{entrada}' NÃO é válida para o campo {tipo_validacao}!")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Exibição no menu no arquivo main.py
def exibir_menu():
    print("\n" + "=" * 45)
    print("Máscaras de Validação (Expressões Regulares)")       
    print("=" * 45)

    print("1 - Validar Nome")
    print("2 - Validar E-mail")
    print("3 - Validar Senha")
    print("4 - Validar CPF")
    print("5 - Validar Telefone")
    print("6 - Validar tudo (Todos os anteriores)")
    print("0 - Sair")

    print("=" * 45)
