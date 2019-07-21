import os


def is_sample_testcase(filename):
	[name,ext] = filename.split('.')
	testcase_type = name[name.find("_")+1:]

	return testcase_type.startswith("sample")


def delete_file(path):
	if os.path.exists(path):
		os.remove(path)


def get_testcase_path(filename):
	path = "data/"
	[fname,ext] = filename.split('.')

	name = fname[:fname.find("_")]
	num = int(fname[fname.rfind("_")+1:])

	if is_sample_testcase(filename):
		path += "sample"
		name += "_sample"
	else:
		path += "secret"

	if ext == "out":
		ext = "ans"

	fname = "{0}_{1:04}.{2}".format(name, num, ext)
	return os.path.join(path, fname)
