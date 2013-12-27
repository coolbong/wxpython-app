import subprocess

p = subprocess.Popen(['ls', '-a', '/dev/input/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = p.communicate()

print out

events = out.split()

if "event6" in events:
	print "True"
else:
	print "False"