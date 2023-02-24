import json

arquivo = open("C:\\Users\\Tuco\\OneDrive\\Área de Trabalho\\ARQUIVO_UNIAO\\dicionario.json", "r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()
agenda = json.loads(conteudo)

print(agenda)