try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='fast2phy',
    description="Convert aligned FASTA format to interleaved PHYLIP format",
    license='MIT',
    author='David M Noriega',
    author_email='davidmnoriega@gmail.com',
    version='1.0',
    install_requires=['numpy', 'pyfasta'],
    packages=['fast2phy'],
    entry_points={
        'console_scripts': ['fast2phy=fast2phy:main']}
    )
