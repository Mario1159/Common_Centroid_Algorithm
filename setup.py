from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Common Centroid Algorithm"
LONG_DESCRIPTION = "Common Centroid Placement using Genetic Algorithm (GA) with the Swap Mutation Technique."

setup(
    name="cca",
    version=VERSION,
    author="Vadim Borisov",
    maintainer="Mario Romero",
    maintainer_email="mario@1159.cl",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
)
