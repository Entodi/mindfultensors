from setuptools import setup

setup(name='mongoslabs',
      version='0.0.1',
      author='Sergey Plis',
      author_email='s.m.plis@gmail.com',
      packages=['mongoslabs'],
      scripts=['scripts/usage_example.py'],
      url='http://pypi.python.org/pypi/mongoslabs/',
      license='LICENSE',
      description='Dataloader that serves MRI images from a mogodb',
      long_description=open('README.md').read(),
      install_requires=[
          "numpy >=1.21",
          "scipy >= 1.7",
          "pymongo >= 4.0",
          "torch >=1.10",
          ""],
    )
