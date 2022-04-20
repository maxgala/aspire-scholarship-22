import sys
import subprocess

# pip install tabulate
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'tabulate'])

# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

# pip install pytest
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pytest'])

# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(installed_packages)

