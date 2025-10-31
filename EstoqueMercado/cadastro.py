import json
import os
import time
from utils import Utils
from dados import salvar_funcionario, carregar_funcionario


class Cadastro:
    @classmethod
    def cadastro(cls):
        print("Cadastro de funcionário")
        nome = input("Digite o nome:\n--> ").capitalize().strip()

        data_nasc = input("Digite a data_nasc [dd/mm/aaaa]:\n--> ")
        while len(data_nasc) != 10:
            print("Data inválida")
            data_nasc = input("Digite a data_nasc [dd/mm/aaaa]:\n--> ")

        cpf = input("Digite o CPF:\n--> ")
        while len(cpf) != 11:
            print("CPF inválido")
            cpf = input("Digite o CPF:\n--> ")

        telefone = input("Digite o telefone:\n--> ")
        while len(telefone) != 11:
            print("Telefone inválido")
            telefone = input("Digite o telefone:\n--> ")

        senha = input("Digite a senha [6 digitos]:\n--> ")
        while len(senha) != 6:
            print("Senha inválida")
            senha = input("Digite a senha [6 digitos]:\n--> ")

        rua = input("Digite a rua:\n--> ")
        numero = int(input("Digite o numero:\n--> "))
        bairro = input("Digite o bairro:\n--> ")
        cep = input("Digite o cep [00000-000]:\n--> ")
        while len(cep) != 9:
            print("CEP inválido")
            cep = input("Digite o cep [00000-000]:\n--> ")
        estado = input("Digite o estado:\n--> ")
        novo_funcionario = {
            "nome": nome,
            "data_nasc": data_nasc,
            "cpf": cpf,
            "telefone": telefone,
            "senha": senha,
            "endereco": {
                "rua": rua,
                "numero": numero,
                "bairro": bairro,
                "cep": cep,
                "estado": estado
            }
        }

        funcionarios = carregar_funcionario(Cadastro)
        funcionarios.append(novo_funcionario)
        salvar_funcionario(Cadastro, funcionarios)
        print("Funcionário cadastrado com sucesso!")