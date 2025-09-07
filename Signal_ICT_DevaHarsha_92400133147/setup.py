from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="signal_ICT_AbhinayChoudhari_92400133174",
    version="1.0.0",
    author="Abhinay Choudhari",
    author_email="abhinay@example.com",
    description="A Python package for signal generation and operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19.5",
        "matplotlib>=3.3.4"
    ],
)
