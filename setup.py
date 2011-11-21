from setuptools import setup

setup(
    name="ningapi",
    version="1.0.2",
    author="Ning Inc.",
    author_email="help@ning.com",
    maintainer='Devin Sevilla',
    url="https://github.com/ning/ning-api-python",
    description=("Python Client for accessing the Ning API"),
    license="Apache License, Version 2.0",
    install_requires=['oauth2'],
    packages=['ningapi', 'tests'],
    test_suite='tests',
    zip_safe=True,
    classifiers=[
              'License :: OSI Approved :: Apache Software License',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7'
              ],
)
