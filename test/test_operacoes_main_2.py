import pytest

from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Carrinho import Carrinho
from classes.Pagamentos import Pagamento

import copy


@pytest.mark.pessoafisica
@pytest.mark.main2
def test_pessoa_fisica_criacao_main2():

    pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')

    assert pessoa.nome == 'Johnson' and pessoa.cpf == 78945623498 and pessoa.email == 'netnet@netnet.com.br' and pessoa.listar_enderecos() == []


@pytest.mark.main2
@pytest.mark.endereco
def test_endereco_cep_str_main2():
    end = Endereco('05447000', 43)

    assert end.rua == 'Rua Caropá'


@pytest.mark.main2
@pytest.mark.endereco
def test_endereco_cep_int_main2():
    end = Endereco(1223010,840)

    assert end.rua == 'Rua General Jardim'


@pytest.mark.main2
@pytest.mark.pessoafisica
def test_pessoa_fisica_adicionar_endereco_e_listar_main2():
    pessoa1 = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')

    end1 = Endereco('05447000', 43)
    end2 = Endereco(1223010,840)

    pessoa1.adicionar_endereco('casa', end1)
    pessoa1.adicionar_endereco('trabalho', end2)

    lista = pessoa1.listar_enderecos()

    assert lista == [f'casa : {end1}',f'trabalho : {end2}']


@pytest.mark.main2
@pytest.mark.produto
def test_produto_criacao_com_nome_main2():
    prod = Produto(2, 'Donuts')
    assert prod.get_nome() == 'Donuts'


@pytest.mark.main2
@pytest.mark.carrinho
def test_carrinho_criacao_main2():
    car = Carrinho()

    assert car.itens == {}


@pytest.mark.main2
@pytest.mark.carrinho
def test_carrinho_adicionar_item_main2():
    sabonete = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete)

    assert carrinho.itens == {sabonete.get_id():1}


@pytest.mark.main2
@pytest.mark.pedido
def test_pedido_adicionar_endereco_faturamento_e_entrega_main2():
    pessoa1 = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')
    car = Carrinho()

    end1 = Endereco('05447000', 43)
    end2 = Endereco(1223010,840)

    pedido = Pedido(pessoa1,car)
    pedido.endereco_entrega = copy.deepcopy(end1) 
    pedido.endereco_faturamento = copy.deepcopy(end2)

    assert pedido.get_endereco_entrega() == 'casa : São Paulo, SP, Rua Caropá, 43, 05447000' and pedido.get_endereco_faturamento() == end2


@pytest.mark.main2
@pytest.mark.pedido
def test_pagamento_processa_pagamento_com_endereco_e_lista_main2():
    pessoa1 = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')
    car = Carrinho()

    end1 = Endereco('05447000', 43)
    end2 = Endereco(1223010,840)

    pessoa1.adicionar_endereco('casa', end1)
    pessoa1.adicionar_endereco('trabalho', end2)

    lista = pessoa1.listar_enderecos()

    end = lista[0]

    pedido = Pedido(pessoa1,car)
    pedido.endereco_entrega = copy.deepcopy(end) 
    pedido.endereco_faturamento = copy.deepcopy(end)

    pag = Pagamento(pedido)
    pag.processa_pagamento()
    if pag.pagamento_aprovado:
        pedido.status = Pedido.PAGO 
    

    assert pedido.status == 2 and len(lista)>0 and lista[0] == 'casa : São Paulo, SP, Rua Caropá, 43, 05447000'
