arquivo = open("c:\\Users\\Tuco\\OneDrive\\Área de Trabalho\\ARQUIVO_UNIAO\\informacoes_do_casamento.txt", encoding="UTF-8")

#irá mostrar uma linha do conteudo do arquivo, se eu repetir este print, ele irá ler uma proxima linha

#print(arquivo.readline()) ----> está em comentario para não anular o for la na frente

#aqui ele vai dar continuidade a leiura do arquivo, como já houve um print com um readline
#este proximo readlineS irá ler o restante do arquivo

#print(arquivo.readlines()) -----> comentario para mesmo intuito

for linha in arquivo.readlines():
    print(linha)

arquivo.close()    