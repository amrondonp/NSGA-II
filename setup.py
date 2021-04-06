from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'libnsga2',
  version = '0.1.1',
  description = 'A NSGA-II implementation',
  long_description='A NSGA-II implementation',
  url='https://github.com/amrondonp/NSGA-II',
  author='Andres Rondon',
  author_email='amrondonp@gmail.com',
  packages = find_packages(exclude=['contrib', 'docs', 'tests']),
  keywords='nsga2 nsga ga multi-objective',
  license='MIT',
)
