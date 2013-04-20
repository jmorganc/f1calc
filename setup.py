try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Calculate the permutations for the F1 Championship',
    'author': 'Morgan Campbell',
    'url': '',
    'download_url': '',
    'author_email': 'jmorgancampbell@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['f1calc'],
    'scripts': [],
    'name': 'Formula 1 Championship Calculator'
}

setup(**config)
