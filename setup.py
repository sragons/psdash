# coding=utf-8
from setuptools import find_packages, setup

from psdash import __version__

setup(
    name="psdash",
    version=__version__,
    description="Linux system information web dashboard",
    long_description="psdash is a system information web dashboard for linux using data mainly served by psutil",
    classifiers=[
        "Topic :: System :: Monitoring",
        "Topic :: System :: Logging",
        "Topic :: System :: Networking :: Monitoring",
        "Development Status :: 4 - Beta",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "License :: Public Domain",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
    ],
    keywords="linux web dashboard",
    author="Joakim Hamrén",
    author_email="joakim.hamren@gmail.com",
    url="https://github.com/Jahaja/psdash",
    license="CC0",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Flask",
        "psutil",
        "glob2",
        "gevent",
        "zerorpc",
        "netifaces",
        "argparse",
    ],
    test_suite="tests",
    tests_require=["unittest2"],
    entry_points={"console_scripts": ["psdash = psdash.run:main"]},
)
