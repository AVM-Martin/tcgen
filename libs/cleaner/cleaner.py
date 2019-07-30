from cleaner import constants

from common import helper

def delete_testcases():
	helper.delete_file(constants.FILEPATHS["solution_exec"])
	helper.delete_file(constants.FILEPATHS["runner_exec"])
	helper.delete_directory(constants.TESTCASE_DIRECTORY)


def delete_problem_statement():
	helper.delete_file(constants.FILEPATHS["pdf"])


def cleaner():
	delete_problem_statement()
	delete_testcases()
