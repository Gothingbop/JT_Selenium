import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

with open('requirements', 'r') as file:
    requirements = [line.strip() for line in file]

setuptools.setup(
    name="JT_Selenium",
    version="0.0.10",
    author="Jacob Thompson",
    author_email="Gothingbop@gmail.com",
    description="My Selenium API Wrapper/Utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gothingbop/JT_Selenium",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3',
    package_data={
        '': ['requirements'],
    },
    include_package_data=True
)
