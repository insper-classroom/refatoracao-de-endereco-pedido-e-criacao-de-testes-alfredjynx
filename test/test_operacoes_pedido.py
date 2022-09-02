import pytest
from classes.Endereco import Endereco
from classes.Pedido import Pedido
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho

pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')
car = Carrinho()
end = Endereco('05447000', 43)

@pytest.mark.pedido
def test_pedido_criacao():
    pedido = Pedido(pessoa,car)

    assert pedido.pessoa == pessoa and pedido.carrinho == car and pedido.get_endereco_entrega() == None and pedido.get_endereco_faturamento() == None and pedido.status == Pedido.EM_ABERTO


@pytest.mark.pedido
def test_pedido_criacao_vazio():
    with pytest.raises(TypeError): 
        pedido = Pedido()


@pytest.mark.pedido
def test_pedido_criacao_sem_carrinho():
    with pytest.raises(TypeError): 
        pedido = Pedido(pessoa)


@pytest.mark.pedido
def test_pedido_criacao_sem_pessoa():
    with pytest.raises(TypeError): 
        pedido = Pedido(carrinho=car)


@pytest.mark.pedido
def test_pedido_endereco_entrega():
    pedido = Pedido(pessoa,car)
    pedido.endereco_entrega(end)

    assert pedido.get_endereco_entrega() == end


@pytest.mark.pedido
def test_pedido_endereco_faturamento():
    pedido = Pedido(pessoa,car)
    pedido.endereco_faturamento(end)

    assert pedido.get_endereco_faturamento() == end