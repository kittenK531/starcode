import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kepler",  # Replace with your own username
    version="1.0.0",
    author="Ying Chan",
    author_email="k.space.infinity@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    # Refer to requirements.txt for authoritative list of dependencies
    install_requires=[],
)
