from HackerRank.Algorithms.bill_division import solve

def test_return_diferenca_entre_a_soma_das_duas_contas_caso_positivo():
    k = 1
    bill = [3, 10, 2, 9]
    b = 12

    assert solve(bill, k, b) == 5


def test_return_diferenca_entre_a_soma_das_duas_contas_caso_iguais_com_uma_string_bonappetit():
    k = 1
    bill = [3, 10, 2, 9]
    b = 7

    assert solve(bill, k, b) == f'Bon Appetit'
