import pytest
from escola.verificar_notas import calcular_media 


def test_veifica_aprovado_ou_reprovado_media():
 
    test_media = [
        ([10, 10, 10], "Aprovado"),
        ([10, 9, 8], "Aprovado"),
        ([7, 6, 5], "Reprovado"),
        ([4, 5, 6], "Reprovado"),
        ([10, 10, 9], "Aprovado"),
        ([0, 0, 0], "Reprovado"),
        ([5, 5, 5], "Reprovado"),
    ]

    for notas, status in test_media:
        assert calcular_media(notas) == status
    


    
 

