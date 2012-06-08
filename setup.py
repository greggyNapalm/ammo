from setuptools import setup, find_packages


setup(
    name = 'ammo',
    version = '0.1',
    author = 'Gregory Komissarov',
    author_email = 'gregory.komissarov@gmail.com',
    description = 'Input data generator for different load tools',
    license = 'BSD',
    url = 'https://github.com/greggyNapalm/ammo',
    keywords = ['phantom', 'lunapark', 'ammo'],
    packages = [
        'ammo',
        'ammo.lunapark',
    ],
    zip_safe = False,
    install_requires = [
        'setuptools',
        'jinja2',
        # -*- Extra requirements: -*-
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Lunapark',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
