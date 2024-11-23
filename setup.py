from setuptools import setup, find_packages

setup(
    name="llm_alignment_assistant",
    version="0.1.0",
    author="Your Name",
    description="An LLM Alignment Assistant application.",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "datasets",
        "fastapi",
        "uvicorn"
    ],
)