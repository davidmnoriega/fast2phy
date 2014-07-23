try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
          'description': 'Convert aligned fasta format to interleaved phylip format',
          'license': 'MIT',
          'author': 'David M Noriega',
          'author_email': 'davidmnoriega@gmail.com',
          'version': '0.1.dev',
          'install_requires': ['numpy', 'pyfasta'],
          'packages': ['fast2phy'],
          'name': 'fast2phy'
          }

setup(**config)