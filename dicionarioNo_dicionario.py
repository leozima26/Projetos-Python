contatos = {
    "Bianca Ueda":{
        "celular":"83052907",
        "email":"biaueda16@"
    },
    "Mauricio Leite":{
        "celular":"52432907",
        "email":"leitemauricio@"
    },
    "Leonardo Zimmermann":{
        "celular":"51269002",
        "email":"leonardo.zim@"
    }
}
for nome, forma_contatos in contatos.items():
    print("O contato {}".format(nome))
    for forma, valor in forma_contatos.items():
        print("pode ser encontrado pelo seu {} através do {}".format(forma, valor))

    print("\n")   