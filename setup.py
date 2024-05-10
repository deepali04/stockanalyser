from setuptools import setup, find_packages

setup(
    name='stockanalyser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # list of required packages
    ],
    author='Group8',
    author_email='dnagwade@stevens.edu',
    description='A stock analyser',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/deepali04/stockanalyser',
)
