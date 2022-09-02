import pytest
import requests
from classes.Produto import Produto

@pytest.mark.produto
def test_produto_criacao_sem_nome():
    prod = Produto(1)

    assert prod.get_nome() == ''


@pytest.mark.produto
def test_produto_criacao_com_nome():
    prod = Produto(2, 'Donuts')
    assert prod.get_nome() == 'Donuts'



@pytest.mark.produto
def test_produto_criacao_vazio():

    with pytest.raises(TypeError): 
        Produto()


@pytest.mark.produto
def test_produto_busca_nome():
    prod1 = Produto(3, 'Creme Cracker')
    prod2 = Produto(4, 'Mini Donuts')
    prod3 = Produto(5, 'Feijoada Enlatada')

    assert Produto.busca_nome(prod1.get_nome())[0].get_nome() == 'Creme Cracker'


@pytest.mark.produto
def test_produto_set_id():

    prod1 = Produto(3, 'Cracker')
    prod1.set_id(4)

    assert 4 == prod1.get_id()


@pytest.mark.produto
def test_produto_set_nome():

    prod1 = Produto(3, 'Cracker')
    prod1.set_nome('Concha')

    assert 'Concha' == prod1.get_nome()


@pytest.mark.produto
def test_produto_to_dict():
    nome = ''
    id = 9

    prod = Produto(id,nome)

    assert prod.to_dict() == {'id':id, 'nome':nome}