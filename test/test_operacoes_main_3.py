from itertools import product
import pytest

from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Carrinho import Carrinho
from classes.Pagamentos import Pagamento

import copy


@pytest.mark.pessoafisica
@pytest.mark.main3
def test_pessoa_fisica_criacao_main3():

    pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')

    assert pessoa.nome == 'Johnson' and pessoa.cpf == 78945623498 and pessoa.email == 'netnet@netnet.com.br' and pessoa.listar_enderecos() == []

@pytest.mark.main3
@pytest.mark.endereco
def test_endereco_cep_str_main3():
    end = Endereco('05447000', 43)

    assert end.rua == 'Rua Caropá'


@pytest.mark.main3
@pytest.mark.endereco
def test_endereco_cep_int_main3():
    end = Endereco(1223010,840)

    assert end.rua == 'Rua General Jardim'



@pytest.mark.main3
@pytest.mark.pessoafisica
def test_pessoa_fisica_adicionar_endereco_e_listar_main3():
    pessoa1 = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')

    end1 = Endereco('05447000', 43)
    end2 = Endereco(1223010,840)

    pessoa1.adicionar_endereco('casa', end1)
    pessoa1.adicionar_endereco('trabalho', end2)

    lista = pessoa1.listar_enderecos()

    assert lista == [f'casa : {end1}',f'trabalho : {end2}']


@pytest.mark.main3
@pytest.mark.pessoafisica
def test_pessoa_fisica_listar_endereco_vazio():
    pessoa1 = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')

    lista = pessoa1.listar_enderecos()

    assert lista == []


@pytest.mark.main3
@pytest.mark.pessoafisica
def test_pessoa_fisica_busca_nome_valido_main3():
    pessoa1 = PessoaFisica(789450000000,'netenete@netnet.com.br','João')

    pessoas = PessoaFisica.busca_nome('João')

    assert len(pessoas)>0 and pessoas[0].nome == pessoa1.nome


@pytest.mark.main3
@pytest.mark.pessoafisica
def test_pessoa_fisica_busca_nome_invalido_main3():
    pessoa1 = PessoaFisica(789498,'netneti@netnet.com.br','Jo')

    pessoas = PessoaFisica.busca_nome('John')

    assert len(pessoas)==0 and pessoas == []


@pytest.mark.main3
@pytest.mark.produto
def test_produtos_busca_nome_valido_main3():
    prod = Produto(2, 'Donuts')
    lista = Produto.busca_nome('Donuts')

    assert lista[0] == prod


@pytest.mark.main3
@pytest.mark.produto
def test_produtos_busca_nome_invalido_main3():
    prod = Produto(2, 'Donuts')
    lista = Produto.busca_nome('Don')

    assert lista == []


@pytest.mark.main3
@pytest.mark.pedido
def test_pagamento_processa_pagamento_com_endereco_e_lista_main3():
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
