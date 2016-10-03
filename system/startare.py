import subprocess
import time

while True:
	subprocess.call(["python", "-B", "/usr/share/nginx/html/codiad/workspace/dagar_till_pi/program.py"])
	time.sleep(10)
