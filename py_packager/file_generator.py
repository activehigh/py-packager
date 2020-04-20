
from .collectors import *
from datetime import datetime
import json
import os

class FileGenerator():
    def generate_manifest(self):
        with open("MANIFEST.in", "w") as f:
            # write first part
            with open('./data/MANIFEST.in') as s:
                f.writelines(s.readlines())  
                s.close()   
            f.close()

    def generate_readme(self):
        with open("README.rst", "w") as f:
            # write first part
            with open('./data/README.rst') as s:
                f.writelines(s.readlines())  
                s.close()   
            f.close()

    def generate_requirements(self):
        with open("requirements.txt", "w") as f:
            # write first part
            with open('./data/requirements.txt') as s:
                f.writelines(s.readlines())  
                s.close()   
            f.close()

    def generate_folders(self, prompts):
        name = ""
        for x in prompts:
            if x.key == 'name':
                name = x.answer
        if not os.path.exists("./" + name):
            os.makedirs("./" + name)

        if not os.path.exists("./tests"):
            os.makedirs("./tests")

        if not os.path.exists("./docs"):
            os.makedirs("./docs")

    def generate_setup(self, prompts: list):
        with open("setup-test.py", "w") as f:
            # write first part
            with open('./data/setup') as s:
                f.writelines(s.readlines())  
                s.close()   

            package_details = {}
            for x in prompts:
                package_details[x.key] = x.answer
                if x.key == 'name':
                    package_details['packages'] = [x.answer]
            
            f.write(json.dumps(package_details, sort_keys=True, indent=4))

            # write 2nd part
            with open('./data/setup_2') as s:
                f.writelines(s.readlines())
                s.close()
                
            f.close()
        

    def generate_license(self, prompts):
        name = ""
        for x in prompts:
            if x.key == 'author':
                name = x.answer

        with open('LICENSE', 'w') as f:
            with open("./data/LICENSE", "r") as s:
                lines = s.readlines()
                for line in lines:
                    formatted = line.replace('[YEAR]', str(datetime.now().year))
                    formatted = formatted.replace('[AUTHOR]', name)
                    f.writelines(formatted)
                s.close()
            f.close()


    def generate(self, prompts: list):
        self.generate_setup(prompts)
        self.generate_license(prompts)
        self.generate_folders(prompts)
        self.generate_readme()
        self.generate_manifest()
        self.generate_requirements()
    