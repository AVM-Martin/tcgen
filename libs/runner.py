from cleaner import cleaner

from common import constants

from compressed_problem import compressed_problem

from generate_problem_statement import generate_problem_statement

from generate_testcases import generate_testcases


if __name__ == "__main__":
	try:
		generate_problem_statement.generate_problem_statement()
		generate_testcases.generate_testcases()
		compressed_problem.compressed_problem()
		cleaner.cleaner()

	except AssertionError as e:
		print(e)

	else:
		print("Problemset is ready as", constants.FILEPATHS["zip"])
