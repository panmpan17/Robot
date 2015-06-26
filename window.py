from distutils.core import setup
import py2exe

APP = ['Robot.py']
DATA_FILES = [("source",[]),("level",[])]

setup(
    data_files = DATA_FILES,
    console = APP,
	)