from setuptools import setup, find_packages

setup(
    name='Accessible_Lib',
    version='1.0.0',
    description='Wrappers around AT APIs',
    author='Nancy Pang',
    author_email='npang@mozila.com',
    install_requires=[
        # dependencies
        'comtypes'
    ],
    package_dir={'': 'accessible_lib'},
    packages=find_packages('accessible_lib'),
    include_package_data=True
)
