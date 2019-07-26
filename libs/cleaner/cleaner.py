from cleaner import constants

from common import helper


def cleaner():
	for _, path in constants.FILEPATHS.items():
		helper.delete_file(path)

	helper.subprocess_call(
		args=[
			"rm",
			"-rf",
			constants.TESTCASE_DIRECTORY,
		],
		quiet=True,
	)
