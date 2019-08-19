import os
import shutil
import subprocess


def rename_file(source_path, destination_path):
	try:
		os.rename(source_path, destination_path)
		return True
	except FileNotFoundError:
		return False


def copy_file(source_path, destination_path):
	try:
		shutil.copy2(source_path, destination_path)
		return True
	except FileNotFoundError:
		return False


def delete_file(path):
	try:
		os.remove(path)
		return True
	except FileNotFoundError:
		return False


def delete_directory(path):
	try:
		shutil.rmtree(path)
		return True
	except FileNotFoundError:
		return False


def is_exist(path):
	return os.path.exists(path)


def get_file_list(path="."):
	try:
		datas = next(os.walk(path))

		return datas[2]
	except StopIteration:
		return None


def get_memory_limit(size):
	return int(size) * 1000 / 1024


def subprocess_call(args, quiet=False):
	if quiet:
		return subprocess.call(
			args,
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL,
		)
	else:
		return subprocess.call(args)


def compile(file, executable, language="cpp"):
	if language == "cpp":
		return subprocess_call(
			args=[
				"g++",
				"-std=c++11",
				"-lm",
				"-o",
				executable,
				file,
			],
			quiet=True,
		)

	elif language == "java":
		pass

	elif language == "py":
		copy_file(file, executable)
		return os.chmod(executable, 0o755)
