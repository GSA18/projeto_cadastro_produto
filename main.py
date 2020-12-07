class produto:
    ID = 0
    nome = ' '
    preco = 0.00

lista = []


def Novoproduto():
    nc = produto()
    nc.ID = int(input('Digite um ID: '))
    nc.nome = input('Digite Nome: ')
    nc.preco = float(input('Digite Precoooo: '))
    print()
    return nc


while True:

    opc = int(input('Cadastrar Produto, digite 1\nConsultar Produto, digite 2 \nOpção: '))
    print()
    if opc == 1:
        banco = (Novoproduto())
        lista.append(banco)
        print('Cadastrado com sucesso! \nID: {} \nNome: {} \nPreco: {} '.format(banco.ID, banco.nome, banco.preco))
        print('-' * 25)
    elif opc == 2:
        consulta = int(input('Digite o ID para consulta:'))
        for i in range(len(lista)):
            if lista[i].ID == consulta:
                print('-' * 25)
                print('Resultado Consulta:')
                print('Nome: {} \nPreco: {}\n'.format(lista[i].nome,lista[i].preco))
                print('-' * 25)
               # op2 = int(input('Atualizar Produto, digite 3\nDeletar Produto, digite 4 \nOpção: '))



                break
            else:
                print('Não contém')

