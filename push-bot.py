import subprocess

subprocess.run('git add .', shell=True)
commit=input("Enter commit")
subprocess.run('git commit -m '+ '"' + commit + '"' +' ', shell=True)
branch=input("Enter branch")
subprocess.run('git push -u origin '+branch+' ', shell=True)
