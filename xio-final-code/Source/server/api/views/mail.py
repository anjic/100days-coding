import smtplib
from smtplib import SMTP
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from lib.client_response import ClientResponse
from xio_ise.local_settings import CONF_DIR
from xio_ise.email_conf import EmailConfig

res_obj = ClientResponse()

class SendMail(APIView):
	"""docstring for SendMail"""

	def post(self, request, format=None):
		"""docstring for post"""
		email = EmailConfig()
		try:
			to_mail = request.data.get('email')
			smtpserver = smtplib.SMTP(email.EMAIL_HOST,email.EMAIL_PORT)
			smtpserver.ehlo()
			if email.USE_SSL_TL:
				smtpserver.starttls()
				smtpserver.ehlo() # extra characters to permit edit
				smtpserver.login(email.FROM_MAIL, email.EMAIL_HOST_PASSWORD)

			smtpserver.ehlo()
			header = 'To:' + to_mail + '\n' + 'From: ' + email.FROM_MAIL + '\n' + 'Subject:XIO Test Mail \n'
			message = header + '\n This is XIO test mail  \n\n'
			smtpserver.sendmail(email.FROM_MAIL, to_mail, message)
			smtpserver.quit()
			(response, status_code) = res_obj.response_formation("mail sent", status.HTTP_200_OK)
			return Response(response, status=status_code)

		except Exception as e:
			(response, status_code) = res_obj.response_formation(str(e), status.HTTP_400_BAD_REQUEST)
			return Response(response, status=status_code)
	
	def send_custom_mail(self, sub='', mes='', to_mail=[]):

		email = EmailConfig()
		smtpserver = smtplib.SMTP(email.EMAIL_HOST,email.EMAIL_PORT)
		smtpserver.ehlo()
		msg = MIMEMultipart()  

		if email.USE_SSL_TL:
			smtpserver.starttls()
			smtpserver.ehlo() # extra characters to permit edit
			smtpserver.login(email.FROM_MAIL, email.EMAIL_HOST_PASSWORD)

		smtpserver.ehlo()
		subject = sub
		message = mes
		msg['From'] = email.FROM_MAIL
		msg['To'] = ','.join(to_mail)
		msg['Subject'] = subject
		msg.attach(MIMEText(message, 'plain'))
		text=msg.as_string()
		smtpserver.sendmail(email.FROM_MAIL, to_mail, text)
		print 'done!'
		smtpserver.quit()
