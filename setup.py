from setuptools import setup, find_packages

setup(
    name='unit_localizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pynrrd',
        'numpy', 
        'allensdk'
    ],
    author='Josh Hunt',
    author_email='jbhunt303@gmail.com',
    description='A Python package for localizing units from extracellular recordings',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/felsenlab/unit-localizer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
