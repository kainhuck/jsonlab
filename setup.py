import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonlab",
    version="0.1.3",
    author="kainhuck",
    author_email="kainhuck@163.com",
    description="json marshal and unmarshal for custom class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kainhuck/jsonlab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
