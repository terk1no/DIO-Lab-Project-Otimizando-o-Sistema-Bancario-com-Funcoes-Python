# Desafio Lab Project



## OBJETIVO GERAL: 
Separar as funções existentes de saque, depósito e extrato em funções.
Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## 1 - Separar devidamente as funções Depositar, Sacar e Extrato com especificações citadas a seguir:
1.1 - Saque: argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
      Sugestão de retorno: saldo e extrato

1.2 - Depósito: argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato
      Sugestão de retorno: saldo e extrato

1.3 - Extrato: argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo
     Argumentos nomeados: extrato

## 2 - Criação de duas novas funções: criar usuário e criar conta corrente
2.1 - Criar usuário (cliente): armazenar usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço
      onde o endereço é uma string no formato: logradouro - nro - bairro - cidade/sigla estado
      Deve ser armazenado somente os números do CPF também não podendo cadastrar dois usuários com o mesmo CPF

2.2 - Criar conta corrente: armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário
      O número da conta é sequencial, iniciando em 1 e o número da agência é fixo: 0001
      Um usuário pode ter mais de uma conta, mas uma conta não pode ser vinculada a mais de um usuário

#### OBS:
As funções de depósito e saque são independetes em relação as funções de clientes e contas corrente, portanto nenhum cliente possui um saldo individual, essa função não foi implementada pois não era o objetivo do desafio.
