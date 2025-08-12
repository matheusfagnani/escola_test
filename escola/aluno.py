def calcular_media(notas:list[float]) ->float:



    # validando se a entrada é uma lista 
    if not isinstance (notas,list):
        raise TypeError("nota invalida")
    # validando lista vazia
    if len(notas) == 0:
        raise ValueError("não é permitido o valor ")
    media = sum(notas)/len(notas)
    return round(media,1)
    

    

