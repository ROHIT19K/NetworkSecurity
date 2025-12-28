'''
The Setup.py File is an essential part of packaging and Distributing Python Objects. It is used By Setup 
tools (Or Disutils in Older Python Versions) to define the Configuration of Your Projects 
such as its Metadata, Dependdencies and More
'''


from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This Function will return List of Requirements
    """

    requirement_lst:List[str]=[]

    try:
        with open('requirements.txt', 'r') as file:
            # READ LINE BY LINE FROM THE Files
            lines=file.readlines()
            ## Process each Line 
            for line in lines:
                requirement=line.strip()
                # ignore empty line and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Requirements.txt File Not Found")

    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Rohit",
    author_email="rohitk26311@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
