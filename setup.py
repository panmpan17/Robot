from setuptools import setup

APP = ['Robot.py']
DATA_FILES = [('', ['source']), ('', ['level'])]
OPTIONS = {'iconfile':'MyIcon.icns',}
 
setup(
    app = APP,
    data_files = DATA_FILES,
    setup_requires = ['py2app'],
    options = {'py2app': OPTIONS},
)