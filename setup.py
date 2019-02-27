import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="honeywell_hpma115s0",
    version="0.0.3",
    author="Florentin Bulot",
    author_email="f.bulot@soton.ac.uk",
    description="An interface for honeywell HPMA115S0 particulate matter sensors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FEEprojects/honeywell-hpma115s0",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
     python_requires='>=3.3, <4',
     install_requires=['pyserial']
)
