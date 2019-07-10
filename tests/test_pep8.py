import unittest2
import subprocess
import os.path
import logging


MY_DIR = os.path.dirname(__file__)
SOURCES_DIR = MY_DIR + "/../http"


class TestPep8(unittest2.TestCase):

    def test_pep8(self):
        popen = subprocess.Popen(('pep8', SOURCES_DIR), stdout=
subprocess.PIPE, stderr=subprocess.STDOUT)
        (stdout, stderr) = popen.communicate()
        if stdout != "":
            lines = stdout.split("\n")
            for line in lines:
                if line != "":
                    logging.error(line)
            self.fail("pep8 generated some output")


