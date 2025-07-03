from setuptools import setup, find_packages

def read_readme():
    """Reads the README.md file with UTF-8 encoding."""
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="plantbrain-Signalize",
    version="0.1.0",
    author="Himanshu Ranjan",
    author_email="Himanshu.ranjan@algo8.ai",
    description="A signal processing and anomaly detection package by plantBrain with FFT, Kalman Filter, and Wavelet Transform support.",

    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ALGO8AI/plantbrain-Signalize.git",
    project_urls={
        "Documentation": "https://github.com/ALGO8AI/plantbrain-Signalize.git",
        "Source": "https://github.com/ALGO8AI/plantbrain-Signalize.git"
    },
    packages=find_packages(),
    python_requires=">=3.11.0",
    install_requires=[
        "scikit-learn>=1.6.1",
        "pandas>=2.2.3",
        "numpy>=2.1.3",
        "scipy>=1.9.0",  # For signal processing with FFT and Kalman Filter
        "pykalman>=0.9.5",  # For Kalman filter
        "pywt>=1.2.0",  # For wavelet transform
        "matplotlib>=3.10.0"
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    include_package_data=True,
)
