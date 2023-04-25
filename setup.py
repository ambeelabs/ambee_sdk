from setuptools import find_packages, setup
import os

here = os.path.abspath(os.path.dirname(__file__))

long_description = open(os.path.join(here, 'README.md')).read()

setup(
    name="ambee_sdk",
    packages=find_packages(include=["ambee_sdk"]),
    version="0.1.0",
    author="Ambee",
    license="MIT",
    url='',
    description="Python SDK for Ambee's APIs",
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[ "requests", "pandas", "geopandas"
    ],
     classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='ambee climate environment pollen air-quality weather api sdk',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
    include_package_data=True,
)

