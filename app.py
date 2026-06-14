import os

restaurantes = [{'nome':'Sushi','categoria':'Japonesa','ativo':False},
                {'nome':'Macarrão','categoria':'Italiana','ativo':True},
                {'nome':'Pizza','categoria':'Italiana','ativo':False}
                ]

def escolher_opção():
    ''' Solicita e executa a opção escolhida pelo usuario

    Outputs:
    -Executa a opçãoescolhida pelo usuario
    
    '''
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
       opcao_invalida()

def exibir_nome_programa():
    '''
    Exibe o nome do programa
    '''
    print("""
                                            ░█████╗░██████╗░██████╗░
                                            ██╔══██╗██╔══██╗██╔══██╗
                                            ███████║██████╔╝██████╔╝
                                            ██╔══██║██╔═══╝░██╔═══╝░
                                            ██║░░██║██║░░░░░██║░░░░░
                                            ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░    
    """)
    
def exibir_opcoes():
    '''
    Exibe as opções que o usuario deve escolher
    '''
    print(linha("1. Cadastrar Restaurante \n2. Listar Restaurante \n3. Ativar/Desativar Restaurante \n4. Sair"))      

def cadastrar_novo_restaurante():
    '''
    Cadastra novo restaurante

    Inputs: 
    nome_do_restaurante
    categoria

    Outputs:
    Adiciona um novo restaurante
    '''
    exibir_subtitulo("""
                    ░█████╗░░█████╗░██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░██████╗░
                    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
                    ██║░░╚═╝███████║██║░░██║███████║╚█████╗░░░░██║░░░██████╔╝███████║██████╔╝
                    ██║░░██╗██╔══██║██║░░██║██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║██╔══██╗
                    ╚█████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║██║░░██║██║░░██║
                    ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
    """)
    
    nome_do_restaurante = input(linha("Digite o nome do resturante que deseja cadastrar: "))
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    
    dados_do_restaurante = {
        'nome':nome_do_restaurante,
        'categoria':categoria,
        'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"Cadastro do restaurante {nome_do_restaurante} realizado com sucesso")
    voltar_ao_menu_principal()

def lista_restaurantes():
    '''
    Outputs:
    Exibe a lista dos restaurantes
    '''
    
    exibir_subtitulo("""    
                                ██╗░░░░░██╗░██████╗████████╗░█████╗░
                                ██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗
                                ██║░░░░░██║╚█████╗░░░░██║░░░███████║
                                ██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║
                                ███████╗██║██████╔╝░░░██║░░░██║░░██║
                                ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝
    """)
    print(f"{'- Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Inativo'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')    
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    '''
    Altera o estado de um restaurante para ativo ou inativo

    Inputs:
    nome_restaurante

    Outputs:
    Exibe mensagem indicando sucesso

    '''
    exibir_subtitulo("""
                    ░█████╗░░░░░░██╗██╗░░░██╗░██████╗████████╗░█████╗░██████╗░
                    ██╔══██╗░░░░░██║██║░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
                    ███████║░░░░░██║██║░░░██║╚█████╗░░░░██║░░░███████║██████╔╝
                    ██╔══██║██╗░░██║██║░░░██║░╚═══██╗░░░██║░░░██╔══██║██╔══██╗
                    ██║░░██║╚█████╔╝╚██████╔╝██████╔╝░░░██║░░░██║░░██║██║░░██║
                    ╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝
    """)
    
    
    restaurante_encontrado = False
    while restaurante_encontrado == False :
        print('Digite "Sair" para voltar ao menu')
        nome_restaurante = input("Digite o nome do restaurante que sera alterado: ")
        for restaurante in restaurantes:
            if nome_restaurante.lower() == "sair":
                restaurante_encontrado = True
            elif nome_restaurante == restaurante['nome'] and restaurante['ativo'] == False:
                restaurante['ativo'] = not restaurante['ativo']
                print(f"o Restaurante {restaurante['nome']} foi ativado")
                restaurante_encontrado = True
            elif nome_restaurante == restaurante['nome'] and restaurante['ativo'] == True:
                restaurante['ativo'] = not restaurante['ativo']
                print(f"o Restaurante {restaurante['nome']} foi desativado")
                restaurante_encontrado = True        
        if restaurante_encontrado == False:
            print(f"\nNão foi encontrado nenhum restaurante com o nome:{nome_restaurante}")
    if restaurante_encontrado:
        voltar_ao_menu_principal()     

def linha(texto):
    '''
    Cria uma linha de * para decorar a aplicação
    '''
    linha = '*' * (len(texto))
    return f"{linha}\n{texto}\n{linha}\n"

def opcao_invalida():
    '''
    informa quando o usuario envia uma entrada invalida
    '''
    os.system("cls")
    print("""
                                        
                                    ░█████╗░██████╗░░█████╗░░█████╗░░█████╗░
                                    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
                                    ██║░░██║██████╔╝██║░░╚═╝███████║██║░░██║
                                    ██║░░██║██╔═══╝░██║░░██╗██╔══██║██║░░██║
                                    ╚█████╔╝██║░░░░░╚█████╔╝██║░░██║╚█████╔╝
                                    ░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░

                            ██╗███╗░░██╗██╗░░░██╗░█████╗░██╗░░░░░██╗██████╗░░█████╗░
                            ██║████╗░██║██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗
                            ██║██╔██╗██║╚██╗░██╔╝███████║██║░░░░░██║██║░░██║███████║
                            ██║██║╚████║░╚████╔╝░██╔══██║██║░░░░░██║██║░░██║██╔══██║
                            ██║██║░╚███║░░╚██╔╝░░██║░░██║███████╗██║██████╔╝██║░░██║
                            ╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░╚═╝░░╚═╝
    """)
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''
    solicita uma interação do usuario para voltar a tela de escolha de opções

    Inputs:
    solicita que o usuario digite algo
    '''
    print("\nDigite uma tecla para voltar ")
    input()
    main()

def exibir_subtitulo(texto):
    '''
    Imprime o subtitulo da opção

    Inputs:
    texto: str - O texto do subtítulo
    '''

    os.system("cls")
    print(texto)


def finalizar_app():
    exibir_subtitulo("Finalizando")

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opção()
    
    

if __name__ == '__main__':
    main()
       

