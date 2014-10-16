#!/usr/bin/env python3
import os
import sys
from glob import glob
from setuptools import setup,find_packages
from distutils.sysconfig import get_python_lib
# Warn if we are installing over top of an existing installation. This can
# cause issues where files that were deleted from a more recent Django are
# still present in site-packages. See #18115.

# Dynamically calculate the version based on django.VERSION.
packages=find_packages()
package_dir=dict([('prdmgr.%s'%(x),x) for x in packages])
packages=package_dir.keys()
version = '0.0.1'
setup(
    name='prdmgr',
    version=version,
    url='',
    author='huangtao',
    author_email='huangtao.jh@gmail.com',
    description=('My web site'),
    license='GPL',
    packages=packages,
    package_dir=package_dir,
    include_package_data=True,
    scripts=['workmgr.pyw'],
    data_files=[]
)
