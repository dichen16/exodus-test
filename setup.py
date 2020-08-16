from setuptools import setup, find_packages


def get_description():
    return "Integration test and performance test for release tool-chain(Pub&Pulp with Exodus)."


def get_long_description():
    with open("README.md") as readme:
        text = readme.read()

    # Long description is everything after README's initial heading
    idx = text.find("\n\n")
    return text[idx:]


setup(
    name="exodus-test",
    version="0.0.1",
    packages=find_packages(exclude=["integraion_test","performance_test"]),
    package_data={},
    description=get_description(),
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3",
)
