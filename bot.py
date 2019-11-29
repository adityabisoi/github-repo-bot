import subprocess
# subprocess.run('ls -l', shell=True)
# subprocess.run('git init')
# subprocess.run('ls -l', shell=True)
# subprocess.run('cd ../', shell=True)
# def subprocess_cmd(command):
#     process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
#     proc_stdout = process.communicate()[0].strip()
#     print(proc_stdout.decode())

# subprocess_cmd('git init; git add .;git commit -m "First commit"')

subprocess.run('git init', shell=True)
subprocess.run('git add .', shell=True)
subprocess.run('git commit -m "Initial"', shell=True)
subprocess.run('git remote add origin git@github.com:adityabisoi/bot-test.git', shell=True)
subprocess.run('git push -u origin master', shell=True)




