#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    lista_pessoas = []

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.lista_pessoas.append(self)

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[f'{apelido_endereco}'] = end

    def remover_endereco(self, apelido_endereco):
        if apelido_endereco in self.__enderecos.keys():
            del self.__enderecos[apelido_endereco]
        else:
            print("Endereço já não existe dentro dos cadastrados")

    def get_endereco(self, apelido_endereco):
        return self.__enderecos[apelido_endereco]

    def listar_enderecos(self):
        l = []
        for apelido in self.__enderecos.keys():
            print(f'{apelido} : {self.__enderecos[apelido]}')
            print()
            l.append(f'{apelido} : {self.__enderecos[apelido]}')
        
        return l


    @classmethod
    def busca_nome(cls, nome:str):
        lista_final = []

        for pessoa in cls.lista_pessoas:
            print(pessoa.nome)
            if pessoa.nome == nome:
                lista_final.append(pessoa)
        
        
        return lista_final