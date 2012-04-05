from distutils.core import setup, Command
class Pep8py(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable,\
                                '/usr/lib/python2.7/dist-packages/pep8.py',\
                                raw_input("Please input module name \n")])
        raise SystemExit(errno)
class Pyflakespy(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable,\
        '/usr/local/lib/python2.7/dist-packages/pyflakes/scripts/pyflakes.py',\
                                raw_input("Please input module name \n")])
        raise SystemExit(errno)

setup(name='0_prod',
      version='0.9',
      description='Client server app worked thru RabbitMQ server',
      author='Nikolaj Starodubtsev',
      author_email='starodubcevna@gmail.com',
      py_modules=['server', 'client', 'createbase'],
      data_files=['./etc/conf.cnf', 'Readme'],
      scripts=['setconnect.py'],
      cmdclass={'pep8':Pep8py,
                'pyflakes':Pyflakespy}
     )
