from distutils.core import setup, Command
import commands
import sys
import subprocess
class Pep8(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        module ='./0_prod/'+raw_input ("Please insert module name.\n\
                                        client.py\n\
                                        server.py\n\
                                        setconnect.py\n\
                                        createbase.py\n")
        rez = commands.getstatusoutput('pep8 %s' % (module))
        if rez == (0, ''):
            rez = 'No errors'
        raise SystemExit(rez)
class Pyflakes(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        module ='./0_prod/'+raw_input ("Please insert module name.\n\
                                        client.py\n\
                                        server.py\n\
                                        setconnect.py\n\
                                        createbase.py\n")
        rez = commands.getstatusoutput('pyflakes %s' % (module))
        if rez == (0, ''):
            rez = 'No errors'
        raise SystemExit(rez)


class Tests(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        rez = subprocess.call([sys.executable,\
                              'tests/stest.py'])
        raise SystemExit(rez)


class Testc(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        rez = subprocess.call([sys.executable,\
                              'tests/ctest.py'])
        raise SystemExit(rez)


setup(name='0_prod',
      version='0.9',
      description='Client server app worked thru RabbitMQ server',
      author='Nikolaj Starodubtsev',
      author_email='starodubcevna@gmail.com',
      packages=['0_prod'],
     # package_dir={'0_prod':'./0_prod'},
      data_files=['Readme'],
      package_data={'0_prod': ['./etc/conf.cnf']},
      scripts=['setconnect.py'],
      cmdclass={'pep8':Pep8,
                'pyflakes':Pyflakes,
                'stest':Tests,
                'ctest':Testc}
     )
