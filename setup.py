# setup.py

from setuptools import setup, find_packages

setup(
    name="autopush",
    version="0.1.0",
    author="w3cdpass",
    author_email="kupasva@gmail.com",
    description="autopush cli tool allows to run git commands more simpler",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-git-cli",  # Update with your repository URL
    packages=find_packages(),
    install_requires=[
        "gitpython",
        "inquirerpy",
        "rich",
    ],
    entry_points={
        'console_scripts': [
            'autopush=bin.main:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
