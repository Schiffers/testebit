import lzma, os

pasta = "."  # ajuste se necessário
for nome in os.listdir(pasta):
    if nome.endswith(".lzma"):
        with open(nome, "rb") as f:
            data = f.read()
        try:
            saida = lzma.decompress(data, format=lzma.FORMAT_AUTO)
        except Exception as e:
            print(f"Falhou {nome}: {e}")
            continue
        novo_nome = nome.replace(".lzma", "")
        with open(novo_nome, "wb") as f:
            f.write(saida)
        print(f"OK: {novo_nome} ({len(saida)} bytes)")