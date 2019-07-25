from compressed_problem.modules import (
	compress,
	config,
	constants,
)

from common import helper


def compressed_problem():
	helper.delete_file(constants.FILEPATHS["zip"])

	try:
		datas = config.get_problem_config(constants.FILEPATHS["config"])
	except IOError:
		print("{0} not found, you must manually configure".format(
			constants.FILEPATHS["config"],
		))
		datas = config.get_manual_problem_config()

	config.create_ini_file(constants.FILEPATHS["ini"], datas)
	config.create_yml_file(constants.FILEPATHS["yml"], datas)

	compress.create_compressed_problem(datas)

	helper.delete_file(constants.FILEPATHS["ini"])
	helper.delete_file(constants.FILEPATHS["yml"])
