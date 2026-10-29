"""Linguagens com templates; versões do compilador usam o mesmo arquivo-base."""

EXTENSOES = {
    "c": "c",
    "cpp": "cpp",
    "csharp": "cs",
    "clojure": "clj",
    "dart": "dart",
    "elixir": "exs",
    "go": "go",
    "haskell": "hs",
    "java": "java",
    "javascript": "js",
    "julia": "jl",
    "kotlin": "kt",
    "lua": "lua",
    "ocaml": "ml",
    "pascal": "pas",
    "php": "php",
    "python": "py",
    "r": "r",
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala",
    "sql": "sql",
    "swift": "swift",
    "typescript": "ts",
}

ALIASES = {
    "c++": "cpp",
    "c#": "csharp",
    "cs": "csharp",
    "clj": "clojure",
    "ex": "elixir",
    "exs": "elixir",
    "golang": "go",
    "hs": "haskell",
    "js": "javascript",
    "jl": "julia",
    "kt": "kotlin",
    "ml": "ocaml",
    "pas": "pascal",
    "py": "python",
    "rb": "ruby",
    "rs": "rust",
    "postgresql": "sql",
    "ts": "typescript",
}

OPCOES = sorted(set(EXTENSOES) | set(ALIASES))


def normalizar_linguagem(linguagem: str) -> str:
    linguagem = linguagem.strip().lower()
    return ALIASES.get(linguagem, linguagem)
