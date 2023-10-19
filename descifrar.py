def contar_letras_ordenadas(texto):
    frecuencia_letras = {}
    
    for letra in texto:
        if letra.isalpha():
            if letra in frecuencia_letras:
                frecuencia_letras[letra] += 1
            else:
                frecuencia_letras[letra] = 1
    
    letras_ordenadas = sorted(frecuencia_letras, key=lambda letra: frecuencia_letras[letra], reverse=True)
    
    return letras_ordenadas

def sustituir_letras(texto, letra_original, letra_reemplazo):
    texto = texto.replace(letra_original, letra_reemplazo)
    return texto

texto_cifrado = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"

letras_ordenadas = contar_letras_ordenadas(texto_cifrado)

print("Letras ordenadas por frecuencia:", letras_ordenadas)

primer_caracter = letras_ordenadas[0]
segundo_caracter = letras_ordenadas[1]

frecuencia_espanol = ['e', 'a', 'O', 'L', 'S', 'N', 'D', 'R', 'U', 'I', 'T', 'C', 'P', 'M', 'Y', 'Q', 'B', 'H', 'G', 'F', 'V', 'J', 'Ñ', 'Z', 'X', 'K', 'W']

texto_descifrado = sustituir_letras(texto_cifrado, primer_caracter, frecuencia_espanol[0])
texto_descifrado = sustituir_letras(texto_descifrado, segundo_caracter, frecuencia_espanol[1])

print("Texto descifrado:", texto_descifrado)

while True:
    letra_original = input("Escribe una letra o 'exit' para salir: ")
    
    if letra_original == 'exit':
        break
    
    letra_reemplazo = input("Escribe la letra de reemplazo o 'exit' para salir: ")
    
    if letra_reemplazo == 'exit':
        break
    
    if letra_original.isalpha() and letra_reemplazo.isalpha():
        texto_descifrado = sustituir_letras(texto_descifrado, letra_original, letra_reemplazo)
        print("Texto actualizado:", texto_descifrado)