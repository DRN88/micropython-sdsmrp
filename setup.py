import sys

# Remove current dir from sys.path, otherwise setuptools will peek up our module instead of system's.
sys.path.pop(0)
from setuptools import setup

sys.path.append("..")
import sdist_upip

setup(
    name="micropython-udsmrp",
    version="1.0.0",
    description="Simple DSMR Parser module for MicroPython",
    long_description="Simple DSMR Parser module for MicroPython",
    url="https://github.com/DRN88/micropython-udsmrp",
    author="DRN88",
    author_email="gorkhaan@gmail.com",
    maintainer="DRN88",
    maintainer_email="gorkhaan@gmail.com",
    license="MIT",
    cmdclass={"sdist": sdist_upip.sdist},
    packages=["udsmrp"],
)