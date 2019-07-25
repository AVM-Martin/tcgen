import os
import subprocess

from generate_testcases import constants


def generate_testcases():
	subprocess.call(
		[
			"g++",
			"-std=c++11",
			"-lm",
			"-o",
			constants.SOLUTION_EXEC,
			constants.SOLUTION_PATH,
		],
		stdout=subprocess.DEVNULL,
		stderr=subprocess.DEVNULL,
	)

	os.system("tcframe build")

	subprocess.call(
		[os.path.join(os.getcwd(),constants.RUNNER_EXEC)],
		stdout=subprocess.DEVNULL,
		stderr=subprocess.DEVNULL,
	)
