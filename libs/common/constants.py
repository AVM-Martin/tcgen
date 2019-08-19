import os


FILEPATHS = {
	"statement": "statement_dependencies/statement.tex",
	"pdf": "problem.pdf",

	"solution_path": "solution.cpp",
	"solution_exec": "solution",
	"spec_path": "spec.cpp",
	"runner_exec": "runner",

	"config": "config.yml",
	"ini": "domjudge-problem.ini",
	"yml": "problem.yaml",

	"zip": "problems.zip",
}

JOBNAME = "Statement"

KATTIS_FILEPATHS = {
	"sample_testcase": "data/sample",
	"secret_testcase": "data/secret",

	"description": "problem_statement/problem.pdf",
	"domjudge_description": "problem.pdf",
	"ini": "domjudge-problem.ini",
	"yml": "problem.yaml",
}

TCFRAME_COMMAND = "tcframe build"
TCFRAME_HOME = os.environ["TCFRAME_HOME"]

TESTCASE_DIRECTORY = "tc"
