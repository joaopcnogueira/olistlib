import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="olistlib", # Replace with your own username
    version="0.0.1",
    author="João Paulo Nogueira",
    author_email="joaonogueira@fisica.ufc.br",
    description="A facilities packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pandas >= 0.25.3",
        "tqdm",
        "sqlalchemy"
    ],
    python_requires='>=3.6',
)