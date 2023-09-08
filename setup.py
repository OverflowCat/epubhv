from setuptools import setup

setup(
    name="epubhv",
    author="yihong0618",
    author_email="zouzou0208@gmail.com",
    url="https://github.com/yihong0618/epubhv",
    license="MIT",
    version="0.1.0",
    install_requires=["bs4", "cssutils"],
    entry_points={
        "console_scripts": ["epubhv = epubhv.cli:main"],
    },
)
