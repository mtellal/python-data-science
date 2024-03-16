#!/bin/bash

bold='\033[0;1;97m'
default='\033[0m'

function createPackage() {
	echo -e "${bold}Creating ft_package (sdist, bdist_wheel) ...${default}"
	python setup.py sdist bdist_wheel > /dev/null
}

function installPackage() {
	echo -e "${bold}Installing ft_package with pip ...${default}"
	pip install ./dist/ft_package-0.0.1.tar.gz > /dev/null
	pip install ./dist/ft_package-0.0.1-py3-none-any.whl > /dev/null
}

function uninstallPackage() {
	echo -e "${bold}Uninstalling ft_package with pip ...${default}"
	pip uninstall -y ft_package > /dev/null
}


cd ft_package

uninstallPackage
createPackage
installPackage

echo -e "${bold}Showing ft_package info ${default}"
pip show -v ft_package

cd ..

echo -e "${bold}Executing main.py with ft_package ...${default}"
python main.py
