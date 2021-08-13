import sys

# Remove current dir from sys.path, otherwise setuptools will peek up our module instead of system's.
sys.path.pop(0)
from setuptools import setup

sys.path.append("..")
import sdist_upip

setup(
    name="micropython-sdsmrp",
    version="0.1.3",
    description="Simple DSMR Parser module for MicroPython",
    long_description="Simple DSMR Parser module for MicroPython",
    url="https://github.com/DRN88",
    author="Gorkhaan",
    author_email="gorkhaan@gmail.com",
    maintainer="Gorkhaan",
    maintainer_email="gorkhaan@gmail.com",
    license="MIT",
    cmdclass={"sdist": sdist_upip.sdist},
    packages=["sdsmrp"],
)