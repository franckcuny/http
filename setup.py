from setuptools import setup

import http

setup(
    name='http',
    version=http.__version__,
    description='HTTP library for Python',
    long_description=open('README.rst').read(),
    author='Franck Cuny',
    author_email='franck.cuny@gmail.com',
    url='https://github.com/franckcuny/http',
    packages=['http'],
    license='MIT',
    tests_require=['coverage', 'nose', 'unittest2', 'pep8'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ]
)
