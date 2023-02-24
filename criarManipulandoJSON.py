import json

contatos = {
    "Clark Kent":
        {"Celular": "123456", "Email":"super@kryton.com"},
    "Brune Wayne":
        {"Celular": "654321", "Email":"bat@carvena.com.br"}    
}

print(json.dumps(contatos, indent=4))

arquivo = open ("C:\\Users\\Tuco\\OneDrive\\Área de Trabalho\\ARQUIVO_UNIAO\\dicionario.json", "w", encoding="utf-8")
conteudo = json.dumps(contatos, indent=4)
arquivo.write(conteudo)
arquivo.close()