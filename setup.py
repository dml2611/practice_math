from setuptools import setup, find_packages

setup(
    name='practice_math',
    version='0.0.1',
    author='Daisy Lal',
    author_email='daisylal26@gmail.com',
    description='Fun Maths',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dml2611/practice_math',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',  
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
)

