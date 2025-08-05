from setuptools import setup, find_packages

setup(
    name="database",
    version="0.1.0",
    description="Pipeline",
    author="FW",
    packages=find_packages(),  
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "plotly",
        "matplotlib",
        "seaborn",
        "jupyter",       
        "ipykernel",      
        "nbformat>=4.2.0" 
    ],
    python_requires=">=3.8",
)
