import os
import zipfile

from compressed_problem import constants


def is_sample_testcase(filename):
    [name,ext] = filename.split('.')
    testcase_type = name[name.find("_")+1:]

    return testcase_type.startswith("sample")


def get_testcase_path(filename):
    path = "data/"
    [fname,ext] = filename.split('.')

    name = fname[:fname.find("_")]
    try:
        num = int(fname[fname.rfind("_")+1:])
    except ValueError:
        num = 1

    if is_sample_testcase(filename):
        path += "sample"
        name += "_sample"
    else:
        path += "secret"

    if ext == "out":
        ext = "ans"

    fname = "{0}_{1:04}.{2}".format(name, num, ext)
    return os.path.join(path, fname)


def create_compressed_problem(datas):
    zipf = zipfile.ZipFile(
        constants.FILEPATHS["zip"],
        "w",
        zipfile.ZIP_DEFLATED
    )

    testcase_directory = os.walk(constants.TESTCASE_DIRECTORY)

    for roots, _, files in testcase_directory:
        for file in files:
            if (is_sample_testcase(file) and not datas["include_sample"]):
                continue

            testcase_filepath = os.path.join(roots, file)
            testcase_zippath = get_testcase_path(file)

            zipf.write(testcase_filepath, testcase_zippath)

    zipf.write(constants.FILEPATHS["pdf"], "problem_statement/problem.pdf")
    zipf.write(constants.FILEPATHS["pdf"], "problem.pdf")
    zipf.write(constants.FILEPATHS["ini"], "domjudge-problem.ini")
    zipf.write(constants.FILEPATHS["yml"], "problem.yaml")

    zipf.close()
