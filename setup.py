from setuptools import setup


setup(
    entry_points={
        'console_scripts': 'zodb_test = zodb_test:zodb_test',
    },
    install_requires=[
        'ZODB',
        'eye',
    ],
    name='zodb_test',
    py_modules=[
        'zodb_test',
    ],
)
