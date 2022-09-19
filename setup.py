from setuptools import setup

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name='userefuzz',
    version='1.0.0',
    long_description=readme,
    long_description_content_type="text/markdown",
    description='User-Agent and Referer Header SQLI Fuzzer',
    url='https://github.com/root_tanishq/userefuzz',
    author='Tanishq Rathore',
    license='MIT',
    packages=['userefuzz'],
    scripts=['userefuzz/userefuzz'],
    install_requires=['requests==2.28.1'],

    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)

