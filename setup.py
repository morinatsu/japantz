try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'JapanTZ',
    'author': 'Natsuki Mori',
    'url': 'blog.bagend.info',
    'author_email': 'morinatsu@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['japantz'],
    'scripts': [],
    'name': 'japantz',
    'test_suite': 'nose.collector',
    'tests_require': ['nose']
}

setup(**config)
