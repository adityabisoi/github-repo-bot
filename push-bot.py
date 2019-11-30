import subprocess

with open(".gitignore", "a+") as my_file:
    text=my_file.write("\npush-bot.py")
subprocess.run('git add .', shell=True)
commit=input("Enter commit")
subprocess.run('git commit -m '+ '"' + commit + '"' +' ', shell=True)
branch=input("Enter branch")
subprocess.run('git push -u origin '+branch+' ', shell=True)
