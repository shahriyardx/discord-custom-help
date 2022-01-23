from setuptools import find_packages, setup

# See note below for more information about classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="discord-custom-help",
    version="0.0.7",
    description="A help cog for discord bots",
    long_description=open("README.md", encoding="utf-8", mode="r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shahprog/discord-custom-help/",
    author="Md Shahriyar Alam",
    author_email="mdshahriyaralam552@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="discord-custom-help dch discord-help",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
)
