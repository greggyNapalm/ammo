from setuptools import setup, find_packages

from ammo import __version__

setup(
    name = 'ammo',
    version=__version__,
    author = 'Gregory Komissarov',
    author_email = 'gregory.komissarov@gmail.com',
    description = 'Input data generator for different load tools',
    license = 'BSD',
    url = 'https://github.com/greggyNapalm/ammo',
    keywords = ['phantom', 'lunapark', 'ammo'],
    packages = [
        'ammo',
        'ammo.lunapark',
        'ammo.phantom'
    ],
    zip_safe = False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
