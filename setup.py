from setuptools import setup, find_packages

setup(
    name='my-app',
    version='1.0',
    packages=find_packages(),
    install_requires=['Flask', 'requests'],
    tests_require=['unittest'],
    test_suite='tests',
)
