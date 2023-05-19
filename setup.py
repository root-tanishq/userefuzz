from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='userefuzz',
    version='2.2.0',
    long_description=readme(),
    long_description_content_type="text/markdown",
    description='User-Agent and Referer Header SQLI Fuzzer',
    url='https://github.com/root-tanishq/userefuzz',
    author='Tanishq Rathore',
    license='MIT',
    packages=['userefuzz'],
    install_requires=['requests','colorama'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'userefuzz = userefuzz.__main__:main'
        ]
    },
)
