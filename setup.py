"""It's a setup.py"""

import os

import setuptools


def local_file(name):
    # type: (str) -> str
    """Interpret filename as relative to this file."""
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


SOURCE = local_file("src")
README = local_file("README.md")

with open(local_file("src/js_regex/__init__.py")) as o:
    for line in o:
        if line.startswith("__version__"):
            _, __version__, _ = line.split('"')


setuptools.setup(
    name="js-regex",
    version=__version__,
    author="Cipher Tech Solutions",
    author_email="opensource@ciphertechsolutions.com",
    packages=setuptools.find_packages(SOURCE),
    package_dir={"": SOURCE},
    package_data={"": ["py.typed"]},
    url="https://github.com/ciphertechsolutions/js-regex",
    license="MPL 2.0",
    description="A thin compatibility layer to use Javascript regular expressions in Python",
    zip_safe=False,
    install_requires=[],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
        ]
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Software Development :: Testing",
        "Topic :: Text Processing",
        "Typing :: Typed",
    ],
    long_description=open(README).read(),
    long_description_content_type="text/markdown",
    keywords="python javascript regex compatibility",
)
