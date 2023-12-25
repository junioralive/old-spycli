from setuptools import setup, find_packages

setup(
    name='spymovies-cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'pyfzf',
        'py7zr',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'spy-cli=spy_cli.spy_cli:spym_cli',
            'spy-cli.config=spy_cli.config_script:configure',
            'spy-cli-basic=spy_cli.spyclinoserver:spyclinsm', 
            'spy-cli-player=spy_cli.util.player_installer:install_player',
        ],
    },
)
