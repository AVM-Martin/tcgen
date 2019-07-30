from common import helper

from generate_problem_statement import (
	cleaner,
	constants,
	generator,
)


def generate_problem_statement():
	assert (
		generator.batchmode_generator() == 0
	), "Problem description failed to be generated!"

	generator.batchmode_generator()
	generator.batchmode_generator()

	helper.rename_file(
		constants.JOBNAME + ".pdf",
		constants.FILEPATHS["pdf"],
	)

	cleaner.remove_latex_output()
