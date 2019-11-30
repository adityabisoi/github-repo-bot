import subprocess

key=input("Enter HTTP/SSH key")
subprocess.run('git init', shell=True)
subprocess.run('git add .', shell=True)
commit=input("Enter commit")
subprocess.run('git commit -m '+ '"' + commit + '"' +' ', shell=True)
subprocess.run('git remote add origin '+ key + ' ', shell=True)
subprocess.run('git push -u origin master', shell=True)




