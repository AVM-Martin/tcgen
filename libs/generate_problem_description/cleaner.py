from common import helper

from generate_problem_description import constants


def remove_latex_output():
	helper.delete_file(constants.JOBNAME + ".aux")
	helper.delete_file(constants.JOBNAME + ".log")
	helper.delete_file(constants.JOBNAME + ".out")
	helper.delete_file(constants.JOBNAME + ".toc")
