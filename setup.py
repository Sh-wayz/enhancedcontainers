from containers import __version__
from setuptools import find_packages, setup


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='enhanced-containers',
    packages=find_packages(include=['containers']),
    version=__version__,
    description='Enhanced types and data structures.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Sh-wayz/enhanced-containers',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'

)
