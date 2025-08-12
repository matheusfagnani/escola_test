import pytest
from escola.aluno import calcular_media 

def test_calcular_media_enviando_string():
# definindo entrada
    entrada= 'ola'
# executando  a função esperando erro
    with pytest.raises(ValueError,match="nota invalida "):
      calcular_media(entrada)