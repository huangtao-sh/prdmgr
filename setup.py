#!/usr/bin/env python3
import os
import sys
from glob import glob
from setuptools import find_packages
from distutils.core import setup
from distutils.sysconfig import get_python_lib
# Warn if we are installing over top of an existing installation. This can
# cause issues where files that were deleted from a more recent Django are
# still present in site-packages. See #18115.

# Dynamically calculate the version based on django.VERSION.
version = '0.0.1'
scripts=['workmgr.py']
setup(
    name='prdmgr',
    version=version,
    url='',
    author='huangtao',
    author_email='huangtao.jh@gmail.com',
    description=('prdmgr'),
    license='GPL',
    packages=find_packages(),
    package_data={'prdmgr':['workmgr.gui','prdmgr.xml','images/*.*'],
                  },
    include_package_data=True,
    scripts=scripts,
)
from stdlib.setup import create_cmd
create_cmd(scripts)
