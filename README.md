<p align="center">
  <img src="docs/bee-banner.png" alt="bee — abelha metálica em dourado e prata" width="960">
</p>

# bee

Uma ferramenta de terminal pra ajudar na hora de resolver exercícios do beecrowd. Você passa o número do problema e a linguagem, e o bee cria o arquivo com um código inicial, na pasta certa.

Ainda não tá pronto. Por enquanto, dá pra criar exercícios em **C e Rust**. A parte de testar as soluções começou a ser feita, mas ainda precisa de ajustes pra funcionar pelo terminal.

## Usando

Só precisa de Python 3 pra criar os arquivos. Não tem pacote extra pra instalar.

Dentro da pasta do projeto:

```bash
python3 main.py exercice 1168 c
```

Isso cria um `1168.c` com o template de C. Depois é abrir o arquivo e escrever a solução.

Pra Rust:

```bash
python3 main.py exercice 1000 rust
```

Também pode usar `rs` no lugar de `rust`. E sim, o comando se chama `exercice`, escrito desse jeito mesmo.

Se precisar consultar os argumentos:

```bash
python3 main.py --help
python3 main.py exercice --help
```

Por enquanto, os comandos são chamados com `python3 main.py`; ainda não tem um comando `bee` instalado no sistema.

## Onde os arquivos vão parar

As pastas das linguagens ficam **ao lado da pasta `bee`**, não dentro dela:

```text
Projects/
├── bee/
├── c/
│   └── 1168.c
└── rust/
    └── 1000.rs
```

O bee cria essas pastas se elas não existirem. Se já houver uma solução com o mesmo número naquela linguagem, ele avisa e mantém o arquivo que está lá.

O destino depende de onde o projeto está salvo, não de onde você abriu o terminal.

## Linguagens

| Linguagem | Argumento | Situação |
| --- | --- | --- |
| C | `c` | Funcionando |
| Rust | `rust` ou `rs` | Funcionando |
| C++ | `cpp` | Falta o template |
| Python | `python` ou `py` | Falta o template |
| Java | `java` | Falta o template |

As opções sem template já aparecem na ajuda, mas tentar criar um exercício com elas retorna `Erro: template não encontrado.`

## E os testes?

Essa parte ainda está pela metade. O comando `test` existe, mas hoje termina em `TypeError`: a função de teste espera uma entrada e uma saída esperada, e o `main.py` ainda não passa esses argumentos.

Em `test_exercice.py` já tem a base pra compilar com `gcc`, rodar a solução com um limite de dois segundos e comparar a saída. Só que a entrada ainda está fixa em um exemplo do exercício 1168, e a compilação não muda conforme a linguagem escolhida. A comparação também é exata: espaços e quebras de linha contam.

A busca automática de exemplos ainda não foi implementada. Então, por enquanto, é preciso compilar e testar as soluções por fora. O bee também não envia respostas ao beecrowd.

## Por dentro

O projeto é pequeno:

- `main.py` recebe o comando e chama a função correspondente.
- `cli.py` define os comandos e argumentos do terminal.
- `exercice.py` lê o template e cria o arquivo do exercício.
- `test_exercice.py` contém o teste de soluções que está sendo desenvolvido. Apesar do nome, não é uma suíte de testes do projeto.
- `templates/` guarda os códigos iniciais de C e Rust.

## O que falta

- [ ] Fazer o comando `test` receber a entrada e a saída esperada.
- [ ] Tirar a entrada fixa do código de teste.
- [ ] Adicionar os templates de C++, Python e Java.
- [ ] Compilar ou executar cada linguagem com a ferramenta adequada.
- [ ] Buscar os exemplos dos exercícios automaticamente.
