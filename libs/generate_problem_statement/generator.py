from common import helper

from generate_problem_statement import constants


def batchmode_generator():
	return helper.subprocess_call(
		args=[
			"pdflatex",
			"--interaction=batchmode",
			"-jobname=" + constants.JOBNAME,
			"-halt-on-error",
			constants.FILEPATHS["statement"],
		],
		quiet=True,
	)


def interactive_generator():
	return helper.subprocess_call([
		"pdflatex",
		"-jobname=" + constants.JOBNAME,
		constants.FILEPATHS["statement"],
	])
