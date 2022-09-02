import pytest
import requests
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco

end = Endereco('05447000', 43)
end2 = Endereco('01223010',840)

@pytest.mark.pessoafisica
def test_pessoa_fisica_criacao():

    pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')

    assert pessoa.nome == 'Johnson' and pessoa.cpf == 78945623498 and pessoa.email == 'netnet@netnet.com.br' and pessoa.listar_enderecos() == []


@pytest.mark.pessoafisica
def test_pessoa_fisica_criacao_vazio():
    with pytest.raises(TypeError): 
        PessoaFisica()


@pytest.mark.pessoafisica
def test_pessoa_fisica_criacao_sem_nome():
    pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br')

    assert pessoa.nome == 'Visitante'


@pytest.mark.pessoafisica
def test_pessoa_fisica_criacao_vazio_sem_cpf():
    with pytest.raises(TypeError): 
        PessoaFisica(email='netnet@netnet.com.br', nome='Johnson')


@pytest.mark.pessoafisica
def test_pessoa_fisica_criacao_vazio_sem_email():
    with pytest.raises(TypeError): 
        PessoaFisica(78945623498,nome='Johnson')


@pytest.mark.pessoafisica
def test_pessoa_fisica_adicionar_endereco():
    pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')
    pessoa.adicionar_endereco('endereço',end)
    lista = pessoa.listar_enderecos()

    assert lista == [f'endereço : {end}']


@pytest.mark.pessoafisica
def test_pessoa_fisica_remover_endereco_nome_correto():
    pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')
    pessoa.adicionar_endereco('endereço',end)
    pessoa.remover_endereco('endereço')
    lista = pessoa.listar_enderecos()

    assert lista == []


@pytest.mark.pessoafisica
def test_pessoa_fisica_remover_endereco_nome_errado():
    pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')
    pessoa.adicionar_endereco('endereço',end)
    pessoa.remover_endereco('enderecccccco')
    lista = pessoa.listar_enderecos()

    assert lista == [f'endereço : {end}']


@pytest.mark.pessoafisica
def test_pessoa_fisica_get_endereco():
    pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')
    pessoa.adicionar_endereco('endereço',end)
    pessoa.adicionar_endereco('endereço 2',end2)
    endereco = pessoa.get_endereco('endereço')

    assert endereco == end


@pytest.mark.pessoafisica
def test_pessoa_fisica_listar_enderecos():
    pessoa = PessoaFisica(78945623498,'netnet@netnet.com.br','Johnson')
    pessoa.adicionar_endereco('endereço',end)
    pessoa.adicionar_endereco('endereço 2',end2)
    lista = pessoa.listar_enderecos()

    assert lista == [f'endereço : {end}',f'endereço 2 : {end2}']



@pytest.mark.pessoafisica
def test_pessoa_fisica_busca_nome_existe():

    pessoa = PessoaFisica(78945623498,'netne@netnet.com.br','Johnson')
    pessoa2 = PessoaFisica(78945623598,'netnt@netnet.com.br','Wilson')
    pessoa3 = PessoaFisica(78945623398,'netet@netnet.com.br','Barney')
    pessoa4 = PessoaFisica(78945623298,'nenet@netnet.com.br','William')

    nome = PessoaFisica.busca_nome('Wilson')

    assert nome == [pessoa2]


@pytest.mark.pessoafisica
def test_pessoa_fisica_busca_nome_nao_existe():

    pessoa = PessoaFisica(78945623498,'netne@netnet.com.br','Johnson')
    pessoa2 = PessoaFisica(78945623598,'netnt@netnet.com.br','Wilson')
    pessoa3 = PessoaFisica(78945623398,'netet@netnet.com.br','Barney')
    pessoa4 = PessoaFisica(78945623298,'nenet@netnet.com.br','William')

    nome = PessoaFisica.busca_nome('Charlie')

    assert nome == []