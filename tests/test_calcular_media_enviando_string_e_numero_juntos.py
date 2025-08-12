import pytest 
from escola.aluno import calcular_media

def test_calcular_media_enviando_string_e_numero_juntos():
# definindo entrada
    entrada=['ola',3.0]
# executando  a função esperando erro
    with pytest.raises(TypeError,match=" não é permitido numero e texto "):
        calcular_media(entrada)


    
def test_calcular_media_com_numero_negativo():
    entrada=['0,-10']
# executando  a função esperando erro
    with pytest.raises(TypeError,match=" não é permitido numeo negativo "):
        calcular_media(entrada)
    





def test_calcular_media_com_numero_maior_que_10():
    entrada=[8.0,10,11]
    # executando  a função esperando erro
    with pytest.raises(TypeError,match=" limite de nota\[0,10\]"):
        calcular_media(entrada)




