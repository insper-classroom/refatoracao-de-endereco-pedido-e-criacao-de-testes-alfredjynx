import pytest
from classes.Carrinho import Carrinho
from classes.Produto import Produto

prod = Produto(5, 'Feijoada Enlatada')

@pytest.mark.carrinho
def test_carrinho_criacao():
    car = Carrinho()

    assert car.itens == {}


@pytest.mark.carrinho
def test_carrinho_adicionar_produto_sem_qtd():
    car = Carrinho()
    car.adicionar_item(prod)

    assert car.itens == {prod.get_id():1}


@pytest.mark.carrinho
def test_carrinho_remover_produto():
    car = Carrinho()
    car.adicionar_item(prod)
    car.remover_item(prod)

    assert car.itens == {}


