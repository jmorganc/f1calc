try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Morgan Campbell',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'jmorgancampbell@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['f1calc'],
    'scripts': [],
    'name': 'Formula 1 Championship Calculator'
}

setup(**config)
