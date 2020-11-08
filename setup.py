from setuptools import setup

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
	name='texfig',
	version='1.0',
	description="Utility to generate PGF vector files from Python's Matplotlib plots to use in LaTeX documents.",
	license='MIT',
	author='Nils Leif Fischer',
	author_email='hello@nilsleiffischer.de',
	url='https://nilsleiffischer.de/texfig/',
	packages=['texfig'],
)
