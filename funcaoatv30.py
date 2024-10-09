# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def calc_media(nota1, nota2, nota3):
    media = float(nota1+nota2+nota3)/3
    return media

def calc_resultado(media):
    if media >= 7:
        return "aprovado"
    else:
        return "reprovado"

nota1 = float(input("digite uma nota "))
nota2 = float(input("digite uma nota "))
nota3 = float(input("digite uma nota "))

result_m = calc_media(nota1, nota2, nota3)
print(result_m)

result_calc = calc_resultado(result_m)
print(result_calc)
