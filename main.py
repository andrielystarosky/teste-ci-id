# main.py
def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    print("Todos os testes passaram!")

if __name__ == "__main__":
    test_soma()