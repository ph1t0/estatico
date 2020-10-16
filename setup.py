import glob
from setuptools import find_packages, setup

setup(
    name='estatico',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=glob.glob('bin/*'),
    install_requires=[
        'flask',
    ],
)
