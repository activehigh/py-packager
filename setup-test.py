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
    "author": "asd",
    "author_email": "asd",
    "description": "asd",
    "license": "asd",
    "name": "asd",
    "packages": [
        "asd"
    ],
    "url": "asd",
    "version": "asd"
}
valueDict['install_requires'] = dependencies
valueDict['zip_safe'] = False

setup(**valueDict)
