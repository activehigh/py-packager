from setuptools import setup
import os

# incldue dependencies
dependencies = []
with os.open("./requirements.txt", "r") as requirements_file:
    for line in requirements_file:
        dependencies.append(line)

setup(name='py-packager',
      version='0.1.0-alpha',
      description='A simple python package init tools',
      url='https://github.com/Activehigh/py-packager',
      author='Mahmudul Islam',
      author_email='mahmud6120@gmail.com',
      license='MIT',
      packages=['py-packager'],
      install_requires=dependencies,
      zip_safe=False)