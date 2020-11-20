from HackerRank.Algorithms.DesignerPDFViewer import solve

def test_se_retorna_a_area_corretamente_com_letras_iguais():
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = 'zaba'

    assert solve(h, word) == 28
    
def test_se_retorna_a_area_da_palavra_letras_diferentes():
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    word = 'abc'

    assert solve(h, word) == 9

