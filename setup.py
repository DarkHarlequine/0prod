from distutils.core import setup, Command
import commands
import sys
import subprocess
from glob import glob


def run_check(command_name):
    dir1 = glob('./0_prod/*.py')
    dir2 = glob('./tests/*.py')
    r_dir = glob('./*.py')
    dir1.extend(dir2)
    dir1.extend(r_dir)
    n = len(dir1)
    i = 0
    while i < n:
        rez1 = commands.getstatusoutput('%(command)s %(type)s' % \
                                        {"command": command_name,\
                                         "type": str(dir1[i])})
        if rez1 == (0, ''):
            rez1 = 'No errors in %s' % str(dir1[i])
            print rez1
        else:
            print '%s \n' % str(rez1)
        i = i + 1


class Pep8(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        run_check('pep8')


class Pyflakes(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        run_check('pyflakes')


class Tests(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        rez = subprocess.call([sys.executable,\
                              './tests/stest.py'])
        raise SystemExit(rez)


class Testc(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        rez = subprocess.call([sys.executable,\
                              './tests/ctest.py'])
        raise SystemExit(rez)


setup(name='0_prod',
      version='0.9',
      description='Client server app worked thru RabbitMQ server',
      author='Nikolaj Starodubtsev',
      author_email='starodubcevna@gmail.com',
      packages=['0_prod'],
     #package_dir={'0_prod':'./0_prod'},
      data_files=['Readme'],
      package_data={'0_prod': ['./etc/conf.cnf']},
      scripts=['setconnect.py'],
      cmdclass={'pep8': Pep8,
                'pyflakes': Pyflakes,
                'stest': Tests,
                'ctest': Testc}
     )
