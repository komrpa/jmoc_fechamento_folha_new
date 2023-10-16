def identificar_imagem_referente_certificado(nome_certificado):
    if nome_certificado == 'FR':
        return 'fr_contabilidade_1.png', 'fr_contabilidade_2.png'
    elif nome_certificado == 'JM':
        return 'jm_contabilidade_s_1.png', 'jm_contabilidade_s_2.png'
    elif nome_certificado == 'JMOC':
        return 'jmoc_1.png', 'jmoc_2.png'
    elif nome_certificado == 'WJ':
        return 'wj_contabilidade_1.png', 'wj_contabilidade_2.png'
    elif nome_certificado == 'LW':
        return 'lw_contabilidade_1.png', 'lw_contabilidade_2.png'
    else:
        return None


# elif nome_certificado == 'RF':
#     return 'rf_contabilidade_1.png', 'rf_contabilidade_2.png'
# elif nome_certificado == 'Jairson Moraes':
#     return 'jairson_moraes_1.png', 'jairson_moraes_2.png'
# elif nome_certificado == 'Willian Cesar':
#     return 'willian_cesar_1.png', 'willian_cesar_2.png'
# elif nome_certificado == 'Rafael Silveira':
#     return 'rafael_silveira_1.png', 'rafael_silveira_2.png'
