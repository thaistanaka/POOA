import argparse

# função que organiza os argumentos passados por linha de comando       
def argParser(listArgs):
    parser = argparse.ArgumentParser()
    for arg in listArgs:
        parser.add_argument("--"+arg)
    return parser.parse_args()