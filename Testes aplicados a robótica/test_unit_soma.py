from soma import soma

def test_soma():
    assert soma(2, 3) == 5  # Verifica se 2 + 3 = 5
    assert soma(-1, 1) == 0 # Verifica se -1 + 1 = 0
    assert soma(0, 0) == 0  # Verifica se 0 + 0 = 0
