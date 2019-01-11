from setuptools import setup

with open("README.md") as fp:
	readme = fp.read()

with open("requirements.txt") as fp:
	requirements = fp.read().splitlines()

setup(
	name="lensmesh",
	author="Eero Molkoselkä",
	author_email="eero.molkoselka@gmail.com",
	url="https://github.com/molkoback/lensmesh",
	packages=["lensmesh"],
	version="0.1.0",
	license="MIT",
	description="Python module for generating 3D lens objects.",
	long_description=readme,
	install_requires=requirements,
	classifiers=[
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3"
	]
)
