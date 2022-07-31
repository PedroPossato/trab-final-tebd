import subprocess
from datetime import datetime

def json_to_turtle():

    process = subprocess.Popen(['java', '-jar', 'jarql-1.0.0.jar', 'news.json', 'transform.query'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    stdout, _ = process.communicate()

    stdout = stdout.decode()

    if stdout:
        with open('results.ttl', 'w') as file:
            file.write(stdout)

    return bool(stdout)
