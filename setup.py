import os

from setuptools import setup
from photorepl import version


def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
        return f.read()

setup(
    name='photoREPL',
    version=version,
    description='Experimental CLI/GUI hybrid raw photo editor',
    author='Sam Whited',
    author_email='sam@samwhited.com',
    maintainer='Sam Whited',
    maintainer_email='sam@samwhited.com',
    url='https://github.com/SamWhited/photorepl',
    packages=['photorepl'],
    keywords=[
        'encoding', 'images', 'photography', 'libraw', 'raw', 'photos',
        'editing', 'graphics'
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Topic :: Multimedia :: Graphics :: Editors :: Raster-Based",
        "Topic :: Multimedia :: Graphics :: Viewers",
        "Environment :: X11 Applications :: GTK",
    ],
    long_description=readme(),
    require=[
        'rawkit'
    ],
    extras_require={
        'GI (when in a venv or gi.repository is not available)': ['pgi >= 0.0.10.1']
    },
)
