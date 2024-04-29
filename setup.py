from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="confluence-report-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=required_packages,
    python_requires=">=3.6",
    author="Daniel Tataru",
    author_email="daniel.tataru@dufour.aero",
    description="A package for generting Confluence reports.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://www.dufour.aero",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)