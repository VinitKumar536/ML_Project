from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'#Install the current project in editable mode when running
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Vinit Jangra',
author_email='vinitjangra536.com',
packages=find_packages(),# Ye source(src) walee function chala dega
install_requires=get_requirements('requirements.txt')# Ye line upar wale function ko call karega jo btayega ki kya kya install krna h in form of list 

)