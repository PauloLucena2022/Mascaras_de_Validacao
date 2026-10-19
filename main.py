import validadores

def main():
    opcoes = {
        "1": ("Nome", validadores.validar_nome, 'Alan Turing'),
        "2": ("E-mail", validadores.validar_email, 'teoria@ufpa.br'),
        "3": ("Senha", validadores.validar_senha, 'te0Ria26'),
        "4": ("CPF", validadores.validar_cpf, '123.456.789-10'),
        "5": ("Telefone", validadores.validar_telefone, '(91) 91234-5678 | (91) 912345678 | 91 912345678')
    }

    while (True):
        validadores.exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            print('Obrigado por utilizar as Máscaras de Validação!')
            break
        elif escolha in opcoes:
            nome_campo, funcao_validadora, exemplo = opcoes[escolha]
            validadores.executar_validacao(nome_campo, funcao_validadora, exemplo)
        elif escolha == "6":
            print('PREENCHIMENTO COMPLETO')
            for tipos in ["1","2","3","4","5"]:
                nome_campo, funcao_validadora, exemplo = opcoes[tipos]
                validadores.executar_validacao(nome_campo, funcao_validadora, exemplo)
        else:
            print("\nOpção Inválida! Tente Novamente!")

if __name__ == '__main__':
    main()
