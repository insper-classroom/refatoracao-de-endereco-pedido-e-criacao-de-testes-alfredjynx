#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------





class Produto:

    lista_produtos = []

    def __init__(self, id_produto, nome=''):

        # a utilização do 'self.__id' significa que o ID é exclusivo da classe, só podendo ser mudado se você utilizar um método dentro da classe (não há possibilidade de mudar diretamente o ID)
        self.__id = id_produto
        self.__nome = nome
        Produto.lista_produtos.append(self)

    
    def set_id(self,id_novo):
        self.__id = id_novo

    def set_nome(self,nome_novo):
        self.__nome = nome_novo

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome


    def to_dict(self):
        return {'id':self.__id, 'nome':self.__nome}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome_novo):
        if nome_novo[0] != 'T' and nome_novo[0] != 't':
            self.__nome = nome_novo

    @nome.getter
    def nome(self):
        return self.__nome
    

    @classmethod
    def busca_nome(cls, nome:str):
        lista_final = []

        for produto in cls.lista_produtos:
            if produto.nome == nome:
                lista_final.append(produto)
            
        
        return lista_final
