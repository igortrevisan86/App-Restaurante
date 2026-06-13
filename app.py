import os

restaurantes = [{'nome':'Sushi','categoria':'Japonesa','ativo':False},
                {'nome':'Macarrão','categoria':'Italiana','ativo':True},
                {'nome':'Pizza','categoria':'Italiana','ativo':False}
                ]

def exibir_nome_programa():
    print("""
                                            ░█████╗░██████╗░██████╗░
                                            ██╔══██╗██╔══██╗██╔══██╗
                                            ███████║██████╔╝██████╔╝
                                            ██╔══██║██╔═══╝░██╔═══╝░
                                            ██║░░██║██║░░░░░██║░░░░░
                                            ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░    
    """)

def exibir_opcoes():
    print(linha("1. Cadastrar Restaurante \n2. Listar Restaurante \n3. Ativar/Desativar Restaurante \n4. Sair"))
    

def escolher_opção():
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
       pass

def cadastrar_novo_restaurante():
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
    exibir_subtitulo("""    
                                ██╗░░░░░██╗░██████╗████████╗░█████╗░
                                ██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗
                                ██║░░░░░██║╚█████╗░░░░██║░░░███████║
                                ██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║
                                ███████╗██║██████╔╝░░░██║░░░██║░░██║
                                ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝
    """)

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante} | {categoria} | {ativo}')    
    voltar_ao_menu_principal()

def alterar_estado_restaurante():

    exibir_subtitulo("""
                    ░█████╗░░░░░░██╗██╗░░░██╗░██████╗████████╗░█████╗░██████╗░
                    ██╔══██╗░░░░░██║██║░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
                    ███████║░░░░░██║██║░░░██║╚█████╗░░░░██║░░░███████║██████╔╝
                    ██╔══██║██╗░░██║██║░░░██║░╚═══██╗░░░██║░░░██╔══██║██╔══██╗
                    ██║░░██║╚█████╔╝╚██████╔╝██████╔╝░░░██║░░░██║░░██║██║░░██║
                    ╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝
    """)
    
    nome_restaurante = input("Digite o nome do restaurante que sera alterado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome'] and restaurante['ativo'] == False:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f"o Restaurante {restaurante['nome']} foi ativado")
        
        elif nome_restaurante == restaurante['nome'] and restaurante['ativo'] == True:
            restaurante_encontrado=True
            restaurante['ativo'] = not restaurante['ativo']
            print(f"o Restaurante {restaurante['nome']} foi desativado")
    if restaurante_encontrado == False:
        print(f"\nNão foi encontrado nenhum restaurante com o nome:{nome_restaurante}")
    voltar_ao_menu_principal()

def linha(texto):
    linha = '*' * (len(texto))
    return f"{linha}\n{texto}\n{linha}\n"

def opcao_invalida():
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
    print("\n                                        Digite uma tecla para voltar ")
    input()
    main()

def exibir_subtitulo(texto):
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
