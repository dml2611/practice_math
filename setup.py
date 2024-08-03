from setuptools import setup, find_packages

setup(
    name='practice_math',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
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
    python_requires='>=3.6',
)

