from distutils.core import setup

setup(name='0_prod',
      version='0.9',
      description='Client server app worked thru RabbitMQ server',
      author='Nikolaj Starodubtsev',
      author_email='starodubcevna@gmail.com',
      py_modules=['server', 'client', 'createbase'],
      data_files=['conf.cnf', 'Readme']
     )
