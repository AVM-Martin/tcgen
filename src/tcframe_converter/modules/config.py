import configparser
import yaml


def get_problem_config(filepath):
	with open(filepath, "r") as infile:
		datas = yaml.safe_load(infile)

	try:
		datas["validator_flags"] = " ".join(datas["validator_flags"])
	except:
		datas["validator_flags"] = ""

	datas["memory_limit"] = int(datas["memory_limit"]) * 1000 / 1024

	return datas


def create_ini_file(filepath, datas):
	data = configparser.ConfigParser()

	data.set("", "probid", "")
	data.set("", "timelimit", str(datas["time_limit"]))
	if datas["special_run"] != "default":
		data.set("", "special_run", str(datas["special_run"]))

	# with open(filepath, "w") as outfile:
	# 	data.write(outfile)

	with open(filepath, "w") as outfile:
		outfile.write("probid=\'\'\n")
		outfile.write("timelimit=\'{0}\'\n".format(
			data["DEFAULT"]["timelimit"],
		))
		if datas["special_run"] != "default":
			outfile.write("special_run='{0}'\n".format(
				data["DEFAULT"]["special_run"],
			))



def create_yml_file(filepath, datas):
	data = dict(
		name = datas["problem_name"],
		validator_flag = datas["validator_flags"],
		limits = dict(
			memory = datas["memory_limit"],
		),
	)

	with open(filepath, "w") as outfile:
		yaml.dump(data, outfile, default_flow_style=False)

	# with open(filepath, "w") as outfile:
	# 	outfile.write("---\n")
	# 	outfile.write("name: {0}\n".format(datas["problem_name"]))
	# 	outfile.write("validator_flags: {0}\n".format(
	# 		datas["validator_flags"],
	# 	))
	# 	outfile.write("limits:\n")
	# 	outfile.write("    memory: {0}\n".format(datas["memory_limit"]))
