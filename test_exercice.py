from pathlib import Path
import subprocess
VERDE = "\033[32m"
VERMELHO = "\033[31m"
AZUL = "\033[34m"
RESET = "\033[0m"


def buscar_exemplos(numero: int):
    raise NotImplementedError(
        "A busca automática de exemplos ainda não foi implementada."
    )

def testar_exercicio(
    numero: int,
    linguagem: str,
    entrada: str,
    esperado: str
):
    extensoes = {
            "c": "c",
            "cpp": "cpp",
            "python": "py",
            "java": "java",
            "rust":"rs",
            "py":"py",
            "rs":"rs",
        }
    aliases = {
        "py": "python",
        "c++": "cpp",
        "rs":"rust",
        }
    linguagem = linguagem.strip().lower()
    linguagem=aliases.get(linguagem,linguagem)
    
    if linguagem not in extensoes:
        print(f"{VERMELHO}Erro: linguagem não suportada.{RESET}")
        return
    
    extensao = extensoes[linguagem]
    root = Path(__file__).resolve().parent
    arquivo = root.parent / linguagem / f"{numero}.{extensao}"



    resultado=subprocess.run(
        ["gcc",str(arquivo),"-o","/tmp/bee_teste"],
        capture_output=True,
        text=True
    )
    if resultado.returncode != 0:
        print("Erro de compilação:")
        print(resultado.stderr)
        return

    print("Compilou com sucesso!")

    try:
        execucao = subprocess.run(
            ["/tmp/bee_teste"],
            input="3\n115380\n2819311\n23456\n",
            capture_output=True,
            text=True,
            timeout=2
        )
    except subprocess.TimeoutExpired:
        print(f"{VERMELHO}Tempo limite excedido.{RESET}")
        return

    if execucao.returncode != 0:
        print(f"{VERMELHO}Erro durante a execução:{RESET}")
        print(execucao.stderr)
        return




    

    if execucao.stdout == esperado:
        print(f"{VERDE}Passou no teste!{RESET}")
    else:
        print(f"{VERMELHO}Saída diferente da esperada.{RESET}")
        print("Esperado:", repr(esperado))
        print("Recebido:", repr(execucao.stdout))





if __name__=="__main__":
    testar_exercicio(1168,"c")