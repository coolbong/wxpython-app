
import subprocess





def earphone_is_connected():
	p = subprocess.Popen(['ls', '-a', '/dev/input/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	input_list =out.split()
	return "event6" in input_list


def audio_play_mp3(path):
	#mpg123 SAMPLE_1.MP3
	p = subprocess.Popen(['mpg123', path, '&'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	print out
	#input_list =out.split()
	#return "event6" in input_list

def audio_stop_mp3():
	p = subprocess.Popen(['pkill', '-STOP', 'mpg123'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()


def chmod(path, mod):
	p = subprocess.Popen(['chmod', path, mod], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	print out

def umount_efs():
	p = subprocess.Popen(["umount", "/factory"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	print out
	print err

def umount_cache():
	p = subprocess.Popen(["umount", "/cache"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	print out
	print err

def systemoff():
	p = subprocess.Popen(["init", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	print out
	print err	


print earphone_is_connected()