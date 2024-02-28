from setuptools import setup, find_packages

setup(
    name='espn-api-orm',
    version='0.1.0',
    packages=find_packages(exclude="tests"),
    install_requires=[
        "pydantic>=2.6.1",
        "requests>=2.31.0"
    ],
    author='TEP',
    author_email='theedgepredictor@gmail.com',
    description="A Python interface for the ESPN API",
    long_description=open('README.md').read(),
    url='https://github.com/theedgepredictor/espn-api-orm',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)