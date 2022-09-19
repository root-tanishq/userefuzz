from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='userefuzz',
    version='1.1.1',
    long_description=readme(),
    long_description_content_type="text/markdown",
    description='User-Agent and Referer Header SQLI Fuzzer',
    url='https://github.com/root-tanishq/userefuzz',
    author='Tanishq Rathore',
    license='MIT',
    packages=['userefuzz'],
    scripts=['userefuzz/userefuzz'],
    install_requires=['requests'],

    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)

