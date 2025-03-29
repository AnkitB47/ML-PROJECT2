from setuptools import find_packages, setup # type: ignore
from typing import List

def get_requirements()-> List[str]:
    # "This function returns list of requirements"
    
    requirement_lst:List[str]=[]
    
    
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_lst
    
print(get_requirements())

setup(
    name="ML-PROJECT2",
    version="0.0.1",
    author="Ankit Bhardwaj",
    author_email="jha.ankit230@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)