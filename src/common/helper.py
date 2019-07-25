import os


def delete_file(path):
	if os.path.exists(path):
		os.remove(path)


def is_exist(path):
	return os.path.exists(path)


def get_memory_limit(size):
	return int(size) * 1000 / 1024
