from setuptools import setup
import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(name='uni-translate',
    version='0.0.4',
    description='Python library to "translate" a variety of unicode special characters to normal text',
    long_description=README,
    long_description_content_type="text/markdown",
    author='anytarseir67',
    url='https://github.com/anytarseir67/uni-translate',
    license="GPLv3",
    packages=['uni_translate'],
    entry_points = {
        'console_scripts': ['uni-translate=uni_translate.cli:main'],
    }
)