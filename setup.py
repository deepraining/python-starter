import io
import re

from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("starter/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="starter",
    version=version,
    url="https://github.com/senntyou/python-starter",
    project_urls={
        "Documentation": "https://github.com/senntyou/python-starter",
        "Code": "https://github.com/senntyou/python-starter",
        "Issue tracker": "https://github.com/senntyou/python-starter/issues",
    },
    license="MIT",
    author="senntyou",
    author_email="jiangjinbelief@163.com",
    description="Python Application Template.",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    packages=["starter"],
    package_dir={"starter": "starter"},
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=[],
    tests_require=[
        "pytest",
        "pytest-httpbin",
        "pytest-cov",
        "pytest-mock",
        "pytest-xdist",
    ],
    extras_require={},
    entry_points={"console_scripts": ["starter = starter.cli:main"]},
)
