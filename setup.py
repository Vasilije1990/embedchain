import setuptools

import embedchain.version


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="embedchain",
    version=embedchain.version.__version__,
    author="Taranjeet Singh",
    author_email="reachtotj@gmail.com",
    description="embedchain is a framework to easily create LLM powered bots over any dataset",  # noqa:E501
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/embedchain/embedchain",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    py_modules=["embedchain"],
    install_requires=[
        "langchain>=0.0.205",
        "requests",
        "openai",
        "chromadb==0.3.26",
        "youtube-transcript-api",
        "beautifulsoup4",
        "pypdf",
        "pytube",
        "lxml",
        "sentence_transformers",
        "docx2txt",
        "pydantic==1.10.8"
    ],
    extras_require={"dev": ["black", "ruff", "isort", "pytest"]},
)
