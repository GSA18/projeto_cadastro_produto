class produto:
    ID = 0
    nome = ' '
    preco = 0.00


lista = []
cont_id = 0


def Novoproduto(cont_id):
    nc = produto()
    nc.ID = cont_id
    nc.nome = input('Digite Nome Produto: ')
    nc.preco = float(input('Digite Preco Produto: '))
    print()
    return nc


while True:

    opc = int(input('=' * 30 + '\nCadastrar Produto, Digite 1\nConsultar Produto, Digite 2\n' + '=' * 30 + '\nOpção:'))

    if opc == 1:
        cont_id = cont_id + 1
        banco = (Novoproduto(cont_id))
        lista.append(banco)
        print('Cadastrado com sucesso! \nID: {} \nNome: {} \nPreco: {} '.format(banco.ID, banco.nome, banco.preco))

    elif opc == 2:
        consulta = int(input('Digite o ID para Consulta:'))
        for i in range(len(lista)):
            if lista[i].ID == consulta:

                print('\nResultado Consulta:')
                print('Nome: {} \nPreco: {}'.format(lista[i].nome, lista[i].preco))

                opc2 = int(
                    input(
                        '*' * 30 + '\nAtualizar Produto, Digite 3\nDeletar Produto, Digite 4 \nContinuar, digite 0\n' + '*' * 30 + ' \nOpção:'))
                if opc2 == 3:
                    lista[i].nome = input("Novo nome:")
                    lista[i].preco = float(input("Novo preco:"))
                    print("Atualizado!!!")
                elif opc2 == 4:
                    lista.pop(i)
                    print("Deletado!!!")
                break
        else:
            print('Não existe produto')
