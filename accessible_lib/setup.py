from setuptools import setup, find_packages

setup(
    name='Accessible_Lib',
    version='1.0.0',
    description='Wrappers around AT APIs',
    author='Nancy Pang',
    author_email='npang@mozila.com',
    url='https://github.com/npsecoding/accessible_lib.git',
    install_requires=[
        # dependencies
        'comtypes'
    ],
    tests_require=[
        # dependencies for unit testing
    ],
    package_dir={'': 'accessible_lib'},
    packages=find_packages('accessible_lib'),
    include_package_data=True,
    test_suite='tests',
)
