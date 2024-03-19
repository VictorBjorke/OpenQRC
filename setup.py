from setuptools import setup

APP = ['openqrc.py']
DATA_FILES = ['qcodes.json']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'OpenQRC',
        'CFBundleDisplayName': 'OpenQRC',
        'CFBundleGetInfoString': "Search and display Q-codes",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
    },
    'packages': [],
    'includes': [],
    'resources': DATA_FILES,
}

setup(
    app=APP,
    name="OpenQRC",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)