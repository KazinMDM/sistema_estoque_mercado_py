import json

class Funcionario:
    __arquivo = "cadastro.json"
    def __init__(self, nome, data_nasc, cpf, telefone, senha, rua, numero, bairro, cep,estado,):
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__cpf = cpf
        self.__telefone = telefone
        self.__senha = senha
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cep = cep
        self.__estado = estado

class Gerente(Funcionario):
    def __init__(self, nome, data_nasc, cpf, telefone, senha, rua, numero, bairro, cep,estado, cargo="Gerente"):
        super().__init__(nome, data_nasc, cpf, telefone, senha, rua, numero, bairro, cep,estado,)
        self.__cargo = cargo

class Caixa(Funcionario):
    def __init__(self, nome, data_nasc, cpf, telefone, senha, rua, numero, bairro, cep,estado, cargo="Caixa"):
        super().__init__(nome, data_nasc, cpf, telefone, senha, rua, numero, bairro, cep,estado,)
        self.__cargo = cargo