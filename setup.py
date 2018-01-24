from setuptools import setup, find_packages
from os.path import dirname, realpath, join

CURRENT_DIR = dirname(realpath(__file__))

with open(join(CURRENT_DIR, "README.rst")) as long_description_file:
    long_description = long_description_file.read()


setup(
    name="uno",
    version="0.1.0",
    url="https://github.com/chatops-bearychat/uno",
    author="Yaoda Liu",
    author_email="shonenada@gmail.com",
    description="A ChatOps framework for BearyChat",
    long_description=long_description,
    zip_safe=False,
    packages=find_packages(exclude=["docs"]),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "bearychat==0.4.1",
        "requests==2.18.4",
        "websocket-client==0.44.0"
    ],
    classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
    ]
)
