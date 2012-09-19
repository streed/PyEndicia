from setuptools import setup, find_packages
setup( name="PyEndicia",
	version="1.0",
	description="Python library to interface with the Endicia Postage API",
	author="Sean Reed",
	author_email="sean@bitpostage.net",
	url="https://github.com/streed/PyEndicia",
	long_description=open("README.txt").read(),
	license="LICENSE.txt",
	packages=find_packages(),
	namespace_packages=["endicia"],
	install_requires=[
		"lxml >= 2.3.4",
		"httplib2 >= 0.7.4",
		"schema >= 0.1.1",
		"inject >= 1.0.1",
		"nose >= 1.1.2"
	],
)

