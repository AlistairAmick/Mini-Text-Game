try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A small text-based adventure game I made when doing exercises for Learn Python The Hard Way by Zed A. Shaw.',
    'author': 'Alistair Amick',
    'url': 'https://github.com/AlistairAmick/Mini-Text-Game',
    'download_url': '',
    'author_email': 'aamickWork@tutamail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mini_text_game'],
    'scripts': [mini_text_game.py],
    'name': 'Mini Text Game' 
}

setup(**config)
