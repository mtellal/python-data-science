from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
        name="ft_package",
        version=VERSION,
        author="Mezyann Tellal",
        author_email="mtellal@student.42.fr",
        url="https://github.com/mtellal/ft_package",
        license='MIT',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
)
