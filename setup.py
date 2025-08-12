from setuptools import setup, find_packages

setup(
    name='datalakesurfer',
    version='0.1.0',
    author='Keshav Kant Singh',
    author_email='masterkeshav@gmail.com',
    description='A Python package for Azure Datalake Storage and Microsoft Fabric Lakehouse, enables format detection and schema retrieval for Iceberg, Delta, and Parquet formats.It also helps identify paritioned columns for parquet datasets.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/keshavksingh/datalakesurfer',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'pyarrowfs-adlgen2==0.2.5',
        'adlfs==2023.12.0',
        'azure-identity==1.17.1',
        'azure-storage-file-datalake==12.17.0',
        'numpy==1.26.4',
        'pandas==1.5.3',
        'pyOpenSSL==24.2.1',
        'cryptography==43.0.1',
        'duckdb==1.1.1',
        'deltalake==0.20.2',
        'pydantic==2.11.7',
    ],
)