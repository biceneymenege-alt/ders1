# ders1
kodland python kursunda oluşturduğum ilk repo
eme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(eme_dict[word])
else:
    print(yok)
    # Kelime eşleşmiyorsa ne yapmalıyız?
