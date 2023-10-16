import smtplib
import ssl
from email.message import EmailMessage
import os
import mimetypes
from log_.gravar_log import registrar_logs_execucao


def send_email_adm_anexo(assunto_email, conteudo='', anexo_email=''):

    try:
        # dados de acesso dos emails
        email_senha = open('config_email/passwords/token', 'r').read()
        # se alterar o email origem, é necessário alterar também a senha no arquivo "mail_password"
        email_origem = 'diogo.rodrigues@komcorp.com.br'
        email_destino = ('diogo.rodrigues@komcorp.com.br')

        assunto = assunto_email
        # body = open(
        #     f'config_email/{conteudo}.txt', 'r', encoding='utf-8').read()
        body = conteudo

        # variável para simplificar as chamadas posteriores da função 'EmailMessage()'
        mensagem = EmailMessage()

        # dados do email
        mensagem['From'] = email_origem
        mensagem['To'] = email_destino
        mensagem['Subject'] = f'ROBOT FOLHA JMOC - {assunto}'

        # estruturação do email (se o corpo do email for do tipo html, incluir o parâmetro subtype='html', ao lado do parâmetro body).
        mensagem.set_content(body)

        # adiciona SSL ao código para garantir a segurança dos dados
        safe = ssl.create_default_context()

        if anexo_email:
            # estruturação de um arquivo anexo
            anexo_path = anexo_email
            anexo_arquivo = os.path.basename(anexo_path)
            mime_type, _ = mimetypes.guess_type(anexo_path)
            mime_type, mime_subtype = mime_type.split('/', 1)

            # adiciona o arquivo anexo ao email
            with open(anexo_path, 'rb') as ap:
                mensagem.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,
                                        filename=os.path.basename(anexo_path))

        # acesso e envio do email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
            smtp.login(email_origem, email_senha)
            smtp.sendmail(email_origem, email_destino, mensagem.as_string())

        registrar_logs_execucao(
            f'Email enviado com sucesso -> {assunto_email}')
    except Exception as e:
        registrar_logs_execucao(
            f'Ocorreu um erro ao enviar email, {assunto_email} ==> erro {e}')
