import subprocess
from datetime import datetime

start = datetime.now()

process = subprocess.Popen(['java', '-jar', 'jarql-1.0.0.jar', 'news.json', 'transform.query'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)

stdout, _ = process.communicate()

stdout = stdout.decode()

if stdout:
    with open('results.ttl', 'w') as file:
        file.write(stdout)

else:
    print("Empty")

print(f"Execução durou {(datetime.now() - start).seconds} segundos.")
