class produto:
    ID = 0
    nome = ' '
    preco = 0.00
    peso = 0.00
    largura= 0.00
    altura=0.00
    desc = ' '
    categoria = ' '

    def get_name(self):
        return self.nome

    def set_name(self, name):
        self.nome = name

    def get_preco(self):
        return self.preco

    def set_preco(self,price):
        self.preco=price

    def get_peso(self):
        return self.peso

    def set_peso(self,p):
        self.peso=p

    def get_largura(self):
        return self.largura

    def set_largura(self,l):
        self.largura=l

    def get_altura(self):
        return self.altura

    def set_altura(self, a):
        self.altura= a

    def get_desc(self):
        return self.desc

    def set_desc(self, d):
        self.desc = d

    def get_categora(self):
        return self.categoria

    def set_categoria(self, c):
        self.categoria = c



class categoria:
    ID_cat = 0
    nome_cat = ' '


lista_prod = []
lista_cat = []

cont_id = 0
cont_id2 = 0
opc = 1


def Novoproduto(cont_id):
    np = produto()
    np.ID = cont_id

    nome = input('Digite Nome Produto: ')
    np.set_name(nome)
    preco=float(input('Digite Preco Produto R$(0.00): '))
    np.set_preco(preco)
    peso = float(input('Peso g (0.00): '))
    np.set_peso(peso)
    largura = float(input('Largura cm (0.00):'))
    np.set_largura(largura)
    altura = float(input('Altura cm (0.00):'))
    np.set_altura(altura)

    np.desc = input('Descricao: ')

    if len(lista_cat) != 0:
        print("Categorias:")
        for i in range(len(lista_cat)):
            print("{}){}".format(lista_cat[i].ID_cat, lista_cat[i].nome_cat))
            j = int(input('Escolha o numero da categoria: '))
            np.set_categoria(lista_cat[j - 1].nome_cat)
    else:
        print("Sem Categoria Cadastradas")
        np.set_categoria('Sem Categoria')

    return np


def Novacategoria(cont_id2):
    nc = categoria()
    nc.ID_cat = cont_id2
    nc.nome_cat = input('Nova Categoria: ')
    return nc


while opc != 0:

    opc = int(input(
        '=' * 30 + '\nCadastrar Produto, Digite 1\nConsultar Produto, Digite 2\nCadastrar Categoria, Digite 3\nSair, Digite 0\n' + '=' * 30 + '\nOpção:'))

    if opc == 1:
        cont_id = cont_id + 1
        banco = (Novoproduto(cont_id))
        lista_prod.append(banco)
        print(
            '\nCadastrado com sucesso! \nID: {} \nNome: {} \nPreco: {} \n Peso: {} \nLargura: {} \n Altura: {} \nDescricao: {} \nCategoria: {}'
                .format(banco.ID, banco.nome, banco.preco,banco.peso,banco.largura,banco.altura,banco.desc,banco.categoria))

    elif opc == 2:
        consulta = int(input('Digite o ID para Consulta:'))
        for i in range(len(lista_prod)):
            if lista_prod[i].ID == consulta:

                print('\nResultado Consulta:')
                print('Nome: {} \nPreco: {}\n Peso: {} \nLargura: {} \n Altura: {} \nDescricao: {} \nCategoria: {}'
                      .format(lista_prod[i].nome, lista_prod[i].preco,lista_prod[i].peso,lista_prod[i].largura,
                              lista_prod[i].altura,lista_prod[i].desc,lista_prod[i].categoria))

                opc2 = input(
                    '*' * 30 + '\nAtualizar Produto, Digite a\nDeletar Produto, Digite d \nContinuar, digite 0\n' + '*' * 30 + ' \nOpção:')
                if opc2 == 'a':
                    lista_prod[i].nome = input("Novo nome:")
                    lista_prod[i].preco = float(input("Novo preco:"))
                    lista_prod[i].desc = input("Nova descricao:")
                    print("Atualizado!!!")
                elif opc2 == 'd':
                    lista_prod.pop(i)
                    print("Deletado!!!")
                break
        else:
            print('Não existe produto')
    elif opc == 3:
        cont_id2 = cont_id2 + 1
        banco2 = (Novacategoria(cont_id2))
        lista_cat.append(banco2)
        print("Lista de Categorias Cadastradas:\n")
        for i in range(len(lista_cat)):
            print("{}){}".format(lista_cat[i].ID_cat, lista_cat[i].nome_cat))
