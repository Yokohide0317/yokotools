from setuptools import setup

install_requires = [
    'ipykernel',
    "jupyter",
    "numpy",
    "pandas",
    "polars",
    "matplotlib",
    "seaborn",
    "japanize_matplotlib",
]

packages = [
    "yokotools"
]

#console_scripts = [
#    'sample_lib_cli=sample_lib_cli.call:main',
#]


setup(
    name='yokotools',
    version='0.0.0',
    packages=packages,
    install_requires=install_requires,
    #entry_points={'console_scripts': console_scripts},
)