#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
                    'feedparser',
                
                ]

test_requirements = [ ]

setup(
    author="Taylor-Jayde Blackstone",
    author_email='t.blackstone@inspyre.tech',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Alerts you when a new notification hits your NationStates feed.",
    entry_points={
        'console_scripts': [
            'ns_feed_bringer=ns_feed_bringer.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ns_feed_bringer',
    name='ns_feed_bringer',
    packages=find_packages(include=['ns_feed_bringer', 'ns_feed_bringer.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tayjaybabee/ns_feed_bringer',
    version='1.0.0-dev1',
    zip_safe=False,
)
