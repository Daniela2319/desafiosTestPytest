import pytest
import os

# Etapa 1 - Adicionar um arquivo com testes para esta exercício


def str_to_bool(string):  # função para converte strings em booleandos
    if string.lower() in ["yes", "y", "1"]:  # lower()converte para letras minúsculas
        return True
    elif string.lower() in ["no", "n", "0"]:
        return False


@pytest.mark.parametrize("string", ["Y", "y", "1", "YES"])
def test_str_to_bool_true(string):
    assert str_to_bool(string) is True


@pytest.mark.parametrize("string", ["N", "n", "0", "NO"])
def test_str_to_bool_false(string):
    assert str_to_bool(string) is False


# Etapa 2 - Executar os testes e explorar o relatório
# comando para executa no terminal entra na /pytest-avancado executa pytest -v test_avanced.py

# Etapa 3 - Mover um teste existente para um acessório


class TestFile:
    # Faz primeiro o teste estas função
    # def setup(self):
    #     with open("/tmp/done", "w") as _f:
    #         _f.write("1")

    # def teardown(self):
    #     try:
    #         os.remove("/tmp/done")
    #     except OSError:
    #         pass

    # def test_done_file(self):
    #     with open("/tmp/done") as _f:
    #         contents = _f.read()
    #     assert contents == "1"
    #
    # depois atualiza esse método acessório em vez dos métodos auxiares ^_^
    def test_f(self, tmpfile):
        path = tmpfile()
        with open(path) as _f:
            contents = _f.read()
        assert contents == "1"


@pytest.fixture
def tmpfile(tmpdir):
    def write():
        file = tmpdir.join("done")
        file.write("1")
        return file.strpath

    return write
