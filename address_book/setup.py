from setuptools import setup, find_packages

setup(name='address_book',
      version='0.0.1',
      entry_points={
            'console_scripts':['address-book=address_book.run:run']
      },
      packages=find_packages(),
      install_requires=[
        'prompt_toolkit',
    ])