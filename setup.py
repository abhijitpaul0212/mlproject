from setuptools import find_packages, setup
from typing import List

HYPEN_E_EDOT = "-e ."

def get_requirements(file_path):
    """
    This function will return list of requirements

    Args:
        file_path (str): _description_

    Returns:
        List[str]: _description_
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if HYPEN_E_EDOT in requirements:
            requirements.remove(HYPEN_E_EDOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    url="https://github.com/abhijitpaul0212/mlproject"
    author='Abhijit',
    author_email='abhijitpaul0102@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)