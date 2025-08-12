import pytest 
from escola.aluno import calcular_media

def test_calcular_media_enviando_string_e_numero_juntos():
# definindo entrada
    entrada=['ola',3.0]
# executando  a função esperando erro
    with pytest.raises(ValueError,match=" não é permitido numero e texto "):
        calcular_media(entrada)
