from importlib_metadata import entry_points
from setuptools import setup, find_packages
import codecs, os, pathlib

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.2'
DESCRIPTION = 'YOUR DESCRIPTION HERE'
LONG_DESCRIPTION = (HERE/"README.md").read_text()

# Setting up
setup(
    name="yoshi_simple_temp",
    version=VERSION,
    author="Yoshi Bansal",
    author_email="<bansalyoshi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url='https://github.com/Yoshibansal/py-package-starter-temp',
    license='MIT',
    packages=['simple'],
    include_package_data=True,
    install_requires=['numpy', 'pandas', 'pyfiglet'],
    keywords=['python', 'simple'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        "console_scripts": [
            "simple=simple.__main__:main",
        ]
    },
)