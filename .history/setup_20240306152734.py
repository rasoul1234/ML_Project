from setuptools import find_packages,setup
def get_requirements(file_path:str) -> List[str]:
    
    
    '''this function wil return the list of requirements'''
    requitements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "")for req in requirements]
    
    
    
setup(
    name="ML_Project",
    version = "0.0.1",
    author='Muhammad Rasoul Sahibzadah',
    author_email = 'rasoul.sahibbzadah@auaf.edu.af',
    pachages = find_packages(),
    install_requres = get_requirements('requirements.txt')
    
    
) 