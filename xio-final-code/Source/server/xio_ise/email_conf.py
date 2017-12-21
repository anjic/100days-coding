from api.models.settings import SMTPConfig
from utility.encryption import encryption, decryption


class EmailConfig():
    '''For accessing default email settings data from database'''

    def __init__(self):
        smtp = SMTPConfig.objects.first()

        if smtp:
            self.EMAIL_HOST = smtp.email_host
            self.EMAIL_HOST_USER = smtp.email_host_user
            self.EMAIL_HOST_PASSWORD = decryption(smtp.email_host_password)
            self.EMAIL_PORT = smtp.email_port
            self.FROM_MAIL = smtp.from_mail
            self.ENABLE_AUTHENTICATION = smtp.enable_authentication
            self.USE_SSL_TL = smtp.use_ssl_tl
        else:
            self.EMAIL_HOST = None
            self.EMAIL_HOST_USER = None
            self.EMAIL_HOST_PASSWORD = None
            self.EMAIL_PORT = None
            self.FROM_MAIL = None
            self.ENABLE_AUTHENTICATION = None
            self.USE_SSL_TL = None


if __name__ == '__main__':
    pass
