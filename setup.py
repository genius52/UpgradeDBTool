from setuptools import setup,find_packages

setup(name='UpgradeDBTool',
      version='1.0',
      py_modules=['UpgradeDBTool'],
      description='Use to update dbwrapper and generate upgrade db script',
      license='LGPL',
      packages=find_packages(),
      script=["MainWindow"],
      )