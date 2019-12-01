#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup

import sys

setup_args = dict(
    name='yam_sort',
    version='1.0',
    author='John Crawford',
    author_email='psp_dev@crawfishpress.com',
    url='https://github.com/Crawfishpress/yam_sort',
    description='does basic diff-ing of YAML files while ignoring key-order',
    license='MIT License',
    zip_safe=False,
    keywords="yaml diff sort",
    long_description=open('README.md').read() + "\n\n",
    long_description_content_type="text/markdown",
    install_requires=['PyYAML==5.1.2'],
    packages=['yam_sort'],
    package_dir={'yam_sort': 'src'},
    entry_points={
        'console_scripts': ['yam_sort=yam_sort.main:main']
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)


def main():
    try:
        setup(**setup_args)
    except Exception as ex:
        err_msg = "Couldn't install package {0}...".format(setup_args['name'])
        print(err_msg)
        err_msg = f"reason: {str(ex)}"
        print(err_msg)
        sys.exit(1)


if __name__ == '__main__':
    main()
