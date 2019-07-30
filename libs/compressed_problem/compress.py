import os
import zipfile

from compressed_problem import constants


def is_sample_testcase(filename):
	return filename.find("_sample") != -1


def get_testcase_path(filename):
	[fname,ext] = filename.split('.')

	if is_sample_testcase(filename):
		path = constants.KATTIS_FILEPATHS["sample_testcase"]

		try:
			[name, _, num] = fname.split('_')
			name += "_sample"
			num = int(num)

		except ValueError:
			[name, _] = fname.split("_")
			name += "_sample"
			num = 1

	else:
		path = constants.KATTIS_FILEPATHS["secret_testcase"]

		try:
			[name, num] = fname.split("_")
			num = int(num)

		except ValueError:
			name = fname
			num = 1

	if ext == "out":
		ext = "ans"

	fname = "{0}_{1:04}.{2}".format(name, num, ext)
	return os.path.join(path, fname)


def create_compressed_problem(datas):
	zipf = zipfile.ZipFile(
		constants.FILEPATHS["zip"],
		"w",
		zipfile.ZIP_DEFLATED
	)

	testcase_directory = os.walk(constants.TESTCASE_DIRECTORY)

	for roots, _, files in testcase_directory:
		for file in files:
			if (is_sample_testcase(file) and not datas["include_sample"]):
				continue

			testcase_filepath = os.path.join(roots, file)
			testcase_zippath = get_testcase_path(file)

			zipf.write(testcase_filepath, testcase_zippath)

	zipf.write(
		constants.FILEPATHS["pdf"],
		constants.KATTIS_FILEPATHS["description"],
	)
	zipf.write(
		constants.FILEPATHS["pdf"],
		constants.KATTIS_FILEPATHS["domjudge_description"],
	)
	zipf.write(
		constants.FILEPATHS["ini"],
		constants.KATTIS_FILEPATHS["ini"],
	)
	zipf.write(
		constants.FILEPATHS["yml"],
		constants.KATTIS_FILEPATHS["yml"],
	)

	zipf.close()
