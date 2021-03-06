from setuptools import setup, find_packages
from pkg_resources import require, DistributionNotFound
import os

try:
    filename = os.path.join(os.path.dirname(__file__), 'README.txt')
    description = file(filename).read()
except:
    description = ''

# Dependency check at run time
# If PIL is not found, then it is added in the ``install_requires`` list
install_requires = []   # Empty list if PIL is found
try:
    try:
        require('PIL')
    except DistributionNotFound:
        require('Image')
except DistributionNotFound:
    install_requires = ['PIL']

version = '0.1.6'

setup(name='cropresize3',
      version=version,
      description="crop and resize an image without doing the math yourself",
      long_description=description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='image',
      author='Jeff Hammel',
      author_email='k0scist@gmail.com',
      url='https://github.com/wasw100/python-cropresize3',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      crop-resize = cropresize:main
      """,
      )
