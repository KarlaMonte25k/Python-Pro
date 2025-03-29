meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "OMG": "Expresion o demostracion de sorpresa o impacto",
            "BFF": "Mejores amiga/os por siempre (Best Friends Forever)",
            "XOXO": "Besos y abrazos",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    #¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
     #¿Qué hacer si no se encuentra la palabra?
    print("No tenemos la descrpcion de la palabra")
