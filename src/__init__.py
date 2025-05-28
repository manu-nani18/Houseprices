from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''

    requirements = []

    with open(file_path) as x:
        requirements = x.readlines()
    print(requirements)
    return requirements

get_requirements("requirements.txt")
