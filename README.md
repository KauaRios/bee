<p align="center">
  <img src="docs/bee-banner.png" alt="bee — abelha metálica em dourado e prata" width="960">
</p>

# bee

Uma ferramenta de terminal pra ajudar na hora de resolver exercícios do beecrowd. Você passa o número do problema e a linguagem, e o bee cria o arquivo com um código inicial, na pasta certa.

Ainda não tá pronto. Já dá pra criar exercícios nas **24 linguagens da tabela abaixo**, incluindo SQL. A parte de testar as soluções começou a ser feita, mas ainda precisa de ajustes pra funcionar pelo terminal.

## Usando

Só precisa de Python 3 pra criar os arquivos. Não tem pacote extra pra instalar.

Dentro da pasta do projeto, use:

```text
python3 main.py exercice <numero> <linguagem>
```

Por exemplo:

```bash
python3 main.py exercice 1168 c
python3 main.py exercice 1000 rs
python3 main.py exercice 1001 py
python3 main.py exercice 1001 js
python3 main.py exercice 1001 kotlin
python3 main.py exercice 2602 sql
```

O primeiro comando cria `1168.c` com o template de C. Depois é abrir o arquivo e escrever a solução. Os outros fazem o mesmo nas linguagens escolhidas.

Use os nomes em minúsculas. Atalhos como `rs`, `py` e `js` valem o mesmo que `rust`, `python` e `javascript`. O subcomando se chama `exercice`, escrito desse jeito mesmo.

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
├── rust/
│   └── 1000.rs
├── python/
│   └── 1001.py
├── javascript/
│   └── 1001.js
├── kotlin/
│   └── 1001.kt
└── sql/
    └── 2602.sql
```

O bee cria essas pastas se elas não existirem. Se já houver uma solução com o mesmo número naquela linguagem, ele avisa e mantém o arquivo que está lá.

Os atalhos usam a pasta do nome completo: `js` salva em `javascript/`, por exemplo. O destino depende de onde o projeto está salvo, não de onde você abriu o terminal.

## Linguagens

Todas as opções abaixo têm template e funcionam com `exercice`. Isso cobre a criação do arquivo; compilar e rodar a solução ainda fica por sua conta.

| Linguagem | Argumentos | Extensão |
| --- | --- | --- |
| C | `c` | `.c` |
| C++ | `cpp`, `c++` | `.cpp` |
| C# | `csharp`, `c#`, `cs` | `.cs` |
| Clojure | `clojure`, `clj` | `.clj` |
| Dart | `dart` | `.dart` |
| Elixir | `elixir`, `ex`, `exs` | `.exs` |
| Go | `go`, `golang` | `.go` |
| Haskell | `haskell`, `hs` | `.hs` |
| Java | `java` | `.java` |
| JavaScript | `javascript`, `js` | `.js` |
| Julia | `julia`, `jl` | `.jl` |
| Kotlin | `kotlin`, `kt` | `.kt` |
| Lua | `lua` | `.lua` |
| OCaml | `ocaml`, `ml` | `.ml` |
| Pascal | `pascal`, `pas` | `.pas` |
| PHP | `php` | `.php` |
| Python | `python`, `py` | `.py` |
| R | `r` | `.r` |
| Ruby | `ruby`, `rb` | `.rb` |
| Rust | `rust`, `rs` | `.rs` |
| Scala | `scala` | `.scala` |
| SQL (PostgreSQL) | `sql`, `postgresql` | `.sql` |
| Swift | `swift` | `.swift` |
| TypeScript | `typescript`, `ts` | `.ts` |

Os templates deixam a estrutura inicial pra você escrever a solução, seguindo os [exemplos do beecrowd](https://judge.beecrowd.com/en/faqs/about/examples). Leia os dados pela entrada padrão e imprima só o que o enunciado pede, sem mensagens como “digite um número”.

A lista reúne as linguagens dos exemplos oficiais e SQL, documentado na [API do beecrowd](https://docs.beecrowd.com/). Versões diferentes de uma linguagem usam o mesmo template; escolha a versão do compilador no site ao enviar. SQL é para os problemas da categoria SQL e o template deixa espaço pra consulta, sem inventar tabelas.

### Um detalhe sobre Java

No Java, a classe se chama `Main` e não tem declaração de `package`. O bee salva o exercício como `1001.java` pra manter a organização por número; pra compilar com `javac`, copie o conteúdo para um arquivo `Main.java` numa pasta de teste. No beecrowd, envie o código mantendo o nome da classe.

## E os testes?

**O comando `test` ainda não funciona pela CLI.** A lista de 24 linguagens vale para a criação de exercícios; o executor ainda usa a lista antiga de C, C++, Python, Java e Rust.

Ao chamar `test` com uma das opções aceitas, ele termina em `TypeError`: a função de teste espera uma entrada e uma saída esperada, e o `main.py` ainda não passa esses argumentos.

Em `test_exercice.py` já tem a base pra compilar com `gcc`, rodar a solução com um limite de dois segundos e comparar a saída. Só que a entrada ainda está fixa em um exemplo do exercício 1168, e a compilação não muda conforme a linguagem escolhida. A comparação também é exata: espaços e quebras de linha contam.

A busca automática de exemplos ainda não foi implementada. Então, por enquanto, é preciso compilar e testar as soluções por fora. O bee também não envia respostas ao beecrowd.

## Por dentro

O projeto é pequeno:

- `main.py` recebe o comando e chama a função correspondente.
- `cli.py` define os comandos e argumentos do terminal.
- `exercice.py` lê o template e cria o arquivo do exercício.
- `test_exercice.py` contém o teste de soluções que está sendo desenvolvido. Apesar do nome, não é uma suíte de testes do projeto.
- `linguagens.py` reúne os nomes, atalhos e extensões usados na criação.
- `templates/` guarda os códigos iniciais das 24 linguagens.

## Adicionando ou ajustando um template

Os arquivos ficam em `templates/template.<extensão>`. Você pode editar o código inicial ali; a mudança vale pros próximos exercícios criados, sem mexer nas soluções existentes.

Pra incluir outra linguagem, cadastre o nome e a extensão em `EXTENSOES`, dentro de `linguagens.py`, e crie o template correspondente. Atalhos entram em `ALIASES`. O comando `exercice` pega suas opções desse cadastro automaticamente.

## O que falta

- [ ] Fazer o comando `test` receber a entrada e a saída esperada.
- [ ] Tirar a entrada fixa do código de teste.
- [ ] Compilar ou executar cada linguagem com a ferramenta adequada.
- [ ] Buscar os exemplos dos exercícios automaticamente.
