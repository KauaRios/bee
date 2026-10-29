import argparse

from linguagens import OPCOES


def ler_argumentos():
    parser = argparse.ArgumentParser(
        prog="bee",
        description="Ferramentas para estudar no beecrowd"
    )

    comandos = parser.add_subparsers(dest="comando", required=True)

    exercice = comandos.add_parser(
        "exercice",
        help="Cria o arquivo de um exercício a partir de um template Ex:exercice 1168 rs, cria " \
        "pasta com exercicio 1168 na linguagem rust"
    )

    exercice.add_argument("numero", type=int)
    exercice.add_argument(
        "linguagem",
        choices=OPCOES
    )

    teste=comandos.add_parser(
        "test",
        help="Testa a solução de um exercicio"
    )
    teste.add_argument("numero",type=int)
    teste.add_argument(
        "linguagem",
        choices=["c", "cpp", "python", "java","rust","rs","py"]
    )

    return parser.parse_args()