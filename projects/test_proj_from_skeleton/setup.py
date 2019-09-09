try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This is the test project created from skeleton',
    'author': 'Andrewkha',
    'url': 'test proj url',
    'download_url': 'Test proj download url',
    'author_email': 'chernyshov.andrey@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['test_proj_from_skeleton'],
    'scripts': [],
    'name': 'test_proj_from_skeleton'
}

setup(**config)
