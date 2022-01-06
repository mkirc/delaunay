import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="delaunay",
    version="1.0.3",
    author="mkirc",
    author_email="m.p.kirchner@gmx.de",
    description="A lightweight delaunay triangulation implementation in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Source Files": "https://github.com/mkirc/delaunay"
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

