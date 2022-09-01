import pytest
import requests
from classes.Endereco import Endereco, SemConexao


@pytest.mark.endereco
def test_endereco_cep_str():
    end = Endereco('05447000', 43)

    assert end.rua == 'Rua Caropá'


@pytest.mark.endereco
def test_endereco_cep_int():

    end = Endereco(5447000, 43)

    assert end.rua == 'Rua Caropá'


@pytest.mark.endereco
def test_endereco_consultar_cep_len_invalid_menor():

    assert False == Endereco.consultar_cep('54470')


@pytest.mark.endereco
def test_endereco_consultar_cep_len_invalid_maior():

    assert False == Endereco.consultar_cep('000000054470')


@pytest.mark.endereco
def test_endereco_consultar_cep_invalido():

    assert False == Endereco.consultar_cep('5547078')


@pytest.mark.endereco
def test_endereco_sem_num():

    with pytest.raises(TypeError): 
        Endereco('05447000')


@pytest.mark.endereco
@pytest.mark.sem_net
def test_sem_conexao():

    with pytest.raises(SemConexao) as x: 
        Endereco.consultar_cep('05447000') 
        assert 'Erro de Conexão' in str(x.value)