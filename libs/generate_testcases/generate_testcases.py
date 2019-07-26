import os

from common import helper

from generate_testcases import constants


def generate_testcases():
	assert (
		helper.is_exist(constants.SOLUTION_PATH)
	), constants.SOLUTION_PATH + " does not exist!"

	helper.compile(constants.SOLUTION_PATH, constants.SOLUTION_EXEC)

	assert (
		helper.is_exist(constants.SPEC_PATH)
	), constants.SPEC_PATH + " does not exist!"

	os.system(constants.TCFRAME_COMMAND)

	assert (
		helper.is_exist(constants.RUNNER_EXEC)
	), constants.RUNNER_EXEC + " failed to be built!"

	helper.subprocess_call(
		args=[os.path.join(os.getcwd(), constants.RUNNER_EXEC)],
		quiet=True,
	)
