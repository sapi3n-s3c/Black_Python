import subprocess

command = "%SystemRoot%\Sysnative\msg.exe * See you spacecowboy"
subprocess.Popen(command, shell=True)