from setuptools import setup
import hyperclient

setup(name='hyperclient',
      version=hyperclient.__version__,
      description='Generic client for hypermedia messages',
      author='Lukas Linhart',
      author_email='bugs@almad.net',
      url='https://github.com/Almad/hypermedia-python-client/',
      packages=['hyperclient'],
      license='MIT',
      test_suite="tests")
