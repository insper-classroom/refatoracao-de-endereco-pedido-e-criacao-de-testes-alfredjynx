import pytest
from classes.Endereco import Endereco


def test_endereco_cep_str():
    end = Endereco('05447000', 43)

    assert end.rua == 'Rua Caropá'


def test_endereco_cep_int():

    end = Endereco( int('05447000') , 43)

    assert end.rua == 'Rua Caropá'


