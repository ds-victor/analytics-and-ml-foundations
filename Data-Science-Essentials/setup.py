from setuptools import setup, find_packages

setup(
    name="data-science-essentials",
    version="1.0.0",
    description="Data Science Essentials Module for the ML Series",
    author="ML Series Contributors",
    install_requires=open("requirements.txt").read().splitlines(),
    packages=find_packages(),
)
