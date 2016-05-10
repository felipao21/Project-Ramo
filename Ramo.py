#!/usr/bin/env python
#
# Hey!
# Projeto RAMO
# Por:
# 		Julio Trasferetti
#		Felipe Marabolí


class Receita:
	id = -1

	list_ingredientes = []

	texto = ""

class Ingrediente:
	qtd = -1
	nome = ""

lista_receitas = []
lista_receitas.append(Receita())
lista_receitas.append(Receita())
lista_receitas.append(Receita())
lista_receitas.append(Receita())
lista_receitas.append(Receita())
lista_receitas.append(Receita())
lista_receitas.append(Receita())
lista_receitas.append(Receita())

for x in lista_receitas:
	print x.id