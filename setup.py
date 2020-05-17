import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
VERSION = '0.0.1'
NAME = ' visma-sign-api-python'

# To install the library, run the following
#
# python setup.py install
#

AUTHOR = 'Yury Sergeev'
AUTHOR_EMAIL = 'sergeevyi@gmail.com'
URL = 'https://github.com/sergeevyi/visma-sign-api-python'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Python bindings for the Visma Sign API v1'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [

]

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )