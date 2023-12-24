from setuptools import setup, find_packages

setup(
    name='spymovies-cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'pyfzf',
        'rich',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'spy-cli=spy_cli.spy_cli:spym_cli',
            'spy-cli.config=spy_cli.config_script:configure',
            'spy-cli-basic=spy_cli.spyclinoserver:spyclinsm',  # assuming you have a main() function in spycli-noserver.py
        ]
    },
)