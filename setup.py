import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tpylib-pkg-toopazo", # Replace with your own username
    version="0.0.2",
    author="toopazo",
    author_email="toopazo@protonmail.com",
    description="Python methods for file and folder operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toopazo/tpylib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)