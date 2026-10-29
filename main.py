from cli import ler_argumentos
from exercice import criar_exercicio
from test_exercice import testar_exercicio



def main():
    args=ler_argumentos()
    if args.comando=="exercice":
        criar_exercicio(args.numero,args.linguagem)
    elif args.comando=="test":
        testar_exercicio(args.numero,args.linguagem)





if __name__=="__main__":
    main()