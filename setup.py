from setuptools import setup, find_packages

setup(
    name='Accessible_Lib',
    version='0.0.1',
    description='Wrappers around AT APIs',
    author='Nancy Pang',
    author_email='npang@mozila.com',
    url='<GITHUB URL>',
    install_requires=[
        # list your dependencies
    ],
    tests_require=[
        # dependencies for unit testing
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    test_suite='tests',
)
