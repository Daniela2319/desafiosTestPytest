import pytest


def admin_command(command, sudo=True):
    """
    Prefixa um comando com `sudo` a menos que explicitamente não seja necessário.
    `command` deve ser uma lista.
    """
    if not isinstance(command, list):
        raise TypeError(
            f"esperava que command fosse uma lista, mas recebeu {type(command)}"
        )
    if sudo:
        return ["sudo"] + command
    return command


class TestAdminCommand:

    @staticmethod
    def command():
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected

    def test_non_list_commands(self):
        with pytest.raises(TypeError) as error:
            admin_command("some command", sudo=True)
        assert (
            error.value.args[0]
            == "esperava que command fosse uma lista, mas recebeu <class 'str'>"
        )


# comando para executa no terminal pytest -v test_exercise.py
