from setuptools import setup, find_packages

setup(
    name='pretty_sphinx',
    version='1.0.2',
    author='Thomas Hiscock',
    author_mail='thomas.hiscock@wanadoo.fr',
    description='A pandoc filter for fixing conversion from sphinx-singlehtml',
    license='MIT',
    keywords='pandoc, filters, sphinx',
    py_modules=['pretty_sphinx'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pretty_sphinx = pretty_sphinx:main',
        ],
    },
    install_requires=['pandocfilters>=1.4']
)
