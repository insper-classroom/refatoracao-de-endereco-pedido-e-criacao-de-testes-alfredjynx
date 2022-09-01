#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

import requests
import json



class SemConexao (Exception):
    def __init__(self):
        self.value = 'Erro de Conexão'


class Endereco: 
    '''
    Endereço de uma pessoa ou conta.
    Esta classe possui overload de Contrutor, caso envie apenas três parametros será encaminhado
    para o contrutor que consulta o cep para encontrar o endereço.
    '''

    lista_end = []

    def __init__(self, cep, numero ,rua='', estado='', cidade='', complemento=''):

        print(numero)

        if (rua == '') or (estado == '') or (cidade == ''):
            end_json = Endereco.consultar_cep(cep)

            self.rua = end_json['logradouro']
            self.estado = end_json['uf']
            self.cidade = end_json['localidade']
            self.numero = numero
            self.complemento = complemento
            self.cep = str(cep)

        else:

            self.rua = rua
            self.estado = estado
            self.cidade = cidade
            self.numero = int(numero)
            self.complemento = complemento
            self.cep = str(cep)
        
        Endereco.lista_end.append(self)


    @classmethod
    def consultar_cep(cls, cep:int or str):
        '''
        Metodo realiza a consulta do cep em uma api publica para obter informações
        como estado, cidade e rua
        '''
        # continuam existindo variaveis locais, nem tudo é propriedade de objeto

        if isinstance(cep,int):
            cep = str(cep)



        if len(cep) < 8 or len(cep) == 8:
            cep = ((8-len(cep))*"0") +cep
        else:
            return False
        

        # end point da API de consulta ao cep
        url_api = f'https://viacep.com.br/ws/{str(cep)}/json/'

        # Sem corpo na requisição
        # Não é necessario nenhum cabeçalho HTTP especial

        # try:
        payload = {}
        headers = {}

        # requisição GET na url de pesquisa do cep. Doc.: https://viacep.com.br/
        try:
            response = requests.request("GET", url_api, headers=headers, data=payload)
        except requests.exceptions.ConnectionError:
            raise SemConexao()

        # converte a resposta json em dict
        json_resp = response.json()

        # except requests.exceptions.ConnectionError:

        #     msg = f'Failure:' 
        #     raise SystemExit(msg)
    

        if json_resp == {"erro": "true"}:
            return False

        else:
            return json_resp

    def __str__(self):
        return f"{self.cidade}, {self.estado}, {self.rua}, {self.numero}, {self.cep}"


    def listar_enderecos(self):
        l = []
        for endereco in Endereco.lista_end():
            print(f'{endereco.cidade} : {endereco.rua}, {endereco.numero}')
            print()
            l.append(f'{endereco.cidade} : {endereco.rua}, {endereco.numero}')
        
        return l


