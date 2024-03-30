dictionary = {"key" : "value",
               "anahtar" : "değer"}
               
meme_dict = {
            "CRİNGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
}


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word in meme_dict.keys():
    print("Bu kelimenin karşılığı:" , meme_dict[word])
    
else:
    print("Kelime eşleşmiyor")
    
