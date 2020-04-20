from setuptools import setup

# inlcude readme
def readme():
    with open('README.rst') as f:
        return f.read()

# incldue dependencies
dependencies = []
with open("requirements.txt", "r") as f:
    for line in f:
        dependencies.append(line)

valueDict = {
    'name':'py-packager',
    'version':'0.1.0-alpha',
    'description':'A simple python package init tools',
    'url':'https://github.com/Activehigh/py-packager',
    'author':'Mahmudul Islam',
    'author_email':'mahmud6120@gmail.com',
    'license':'MIT',
    'packages':['py_packager'],
    'install_requires':dependencies,
    'zip_safe':False
}

setup(**valueDict)