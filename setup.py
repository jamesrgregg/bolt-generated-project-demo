from setuptools import setup

setup(
    name='my-app',
    version='1.0',
    packages=['my_app'],
    install_requires=['Flask', 'requests'],
    tests_require=['unittest'],
    test_suite='tests',
)
