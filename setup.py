import setuptools

setuptools.setup(
    name="pydhdt",
    version="0.1.0",
    url="https://github.com/tmilliman/pydhdt",

    author="Tom Milliman",
    author_email="thomas.milliman@unh.edu",

    description="""package for accessing the UNH laser altimetry database tables"",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
