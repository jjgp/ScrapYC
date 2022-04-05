from setuptools import find_packages, setup

install_requires = [
    "scrapy >= 8.0",
]

extras_require = {
    "dev": [
        "black",
        "flake8 >= 4.0",
        "isort >= 5.9",
        "pre-commit >= 2.16",
        "pytest >= 7.1",
    ],
}

setup(
    name="scrapyc",
    version="0.0.1",
    url="https://github.com/jjgp/scrapyc",
    author="Jason Prasad",
    author_email="jasongprasad@gmail.com",
    description="",
    install_requires=install_requires,
    extras_require=extras_require,
    packages=find_packages(),
    python_requires=">=3.10",
)
