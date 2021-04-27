import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as requirements_file:
    external_packages = requirements_file.read()

setuptools.setup(
    name="Transformer",
    version="0.0.1",
    author="Koosha Tahm",
    author_email="kooshi.ml@gmail.com",
    description="Transformer, Attention is all you need! Used http://nlp.seas.harvard.edu/2018/04/03/attention.html as the main reference.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/koosha-t/Attention_is_ALL_you_need.git",
    project_urls={
        "Bug Tracker": "https://github.com/koosha-t/Attention_is_ALL_you_need/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = external_packages,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)