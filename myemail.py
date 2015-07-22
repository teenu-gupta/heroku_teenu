import smtplib

def sendmailall(flag):

	smtpUser = 'testmail0887@gmail.com'
	smtpPass = 'kr!sh123'

	toAdd = 'teenu.gupta@jaarvis.com'
	fromAdd = smtpUser

	if flag==0:
		subject = 'Python Test'
		header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject:' + subject
		body = '500 error on the URL'

	else:
		subject = 'Python Test'
		header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject:' + subject
		body = 'Status OK'
		
	print header + '\n' + body
	s = smtplib.SMTP('smtp.gmail.com',587)

	s.ehlo()
	s.starttls()
	s.ehlo()

	s.login(smtpUser,smtpPass)
	s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
	s.quit()






