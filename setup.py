from  setuptools import find_packages, setup
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Pratish Zandani"
DESCRIPTION="This is FSDS batch's first ML project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirements
    mention in the requirements.txt

    return : This function is going to return a list which will contain name of librearies mentioned in the requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readline()
        #return requirement_file.readline().remove("-e .") ## This should be used when you have find_packages() in setup function below to install all packages


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES, # or write packages=find_packages()  - which will do same thing
    #    find_packages() will find all the folders in our project for __init__.py file. Any folder having __init__.py file is called package and setup.py is a module.
    install_requires=get_requirements_list()
    #packages=find_packages(),
    #install_requires=get_requirements_list())
)

if __name__=="__main__":
    print(get_requirements_list())