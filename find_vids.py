import os
import sys
import shutil

FILE_EXTS = ['.mpg', '.mkv', '.avi', '.mp4']

start_dir = sys.argv[1]
target_dir = sys.argv[2]

print('Starting dir: ', start_dir)
print('Target dir: ', target_dir)

def move_files(start_dir, target_dir):
	for basedir, dirs, files in os.walk(start_dir):
		for f in files:
			if os.path.splitext(f)[1] in FILE_EXTS:
				print('Moving: ', f)
				try:
					shutil.move(os.path.join(basedir, f), target_dir)
				except shutil.Error:
					print("Skipping: ", f)
		for d in dirs:
			move_files(os.path.join(basedir, d), target_dir)

move_files(start_dir, target_dir)