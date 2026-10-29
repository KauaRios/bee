from pathlib import Path

from linguagens import EXTENSOES, normalizar_linguagem

VERDE = "\033[32m"
VERMELHO = "\033[31m"
AZUL = "\033[34m"
RESET = "\033[0m"


def criar_exercicio(numero: int, linguagem: str):

    linguagem = normalizar_linguagem(linguagem)

    if linguagem not in EXTENSOES:
        print(f"{VERMELHO}Erro: linguagem não suportada.{RESET}")
        return

    extensao = EXTENSOES[linguagem]

    try:
        print(f"{AZUL}Criando exercício {numero} em {linguagem}...{RESET}")

        root = Path(__file__).resolve().parent
        template = root / "templates" / f"template.{extensao}"
        conteudo = template.read_text(encoding="utf-8")

        pasta_linguagem = root.parent / linguagem
        pasta_linguagem.mkdir(parents=True, exist_ok=True)

        arquivo = pasta_linguagem / f"{numero}.{extensao}"

        with open(arquivo, "x", encoding="utf-8") as f:
            f.write(conteudo)

        print(f"{VERDE}Sucesso: exercício criado em {arquivo}{RESET}")

    except FileExistsError:
        print(f"{VERMELHO}Erro: arquivo já existe.{RESET}")

    except FileNotFoundError:
        print(f"{VERMELHO}Erro: template não encontrado.{RESET}")

    except OSError as e:
        print(f"{VERMELHO}Erro ao acessar ou escrever os arquivos: {e}{RESET}")


if __name__ == "__main__":
    criar_exercicio(1111, "c")