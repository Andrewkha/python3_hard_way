try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Andrewkha',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'chernyshov.andrey@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'exercise47'
}

setup(**config)