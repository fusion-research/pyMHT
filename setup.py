from setuptools import setup, find_packages

setup(
    name = 'tomht',
    version = '0.1',
    author = 'Erik Liland',
    author_email = 'erik.liland@gmail.com',
    description = ('An implementation of a track oriented multi hypothesis tracker' +
      'with integer linear programming in Python'),
    license = 'BSD',
    keywords = 'mht tomht radar tracking track-split track split multi target multitarget',
    url = 'http://autosea.github.io/sf/2016/04/15/radar_ais/',
    packages = find_packages(exclude=('examples', 'docs')),
    install_requires = [
        'matplotlib',
        'numpy',
        'scipy',
    ],
)
