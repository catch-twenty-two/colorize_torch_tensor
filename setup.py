from setuptools import setup, find_packages

setup(
    name='colorize_pp_tensor',
    version='0.1.1',
    description='Pretty print PyTorch tensors with colored brackets and scalar highlights.',
    author='Your Name',
    packages=find_packages(),
    install_requires=['torch'],
    entry_points={
        'console_scripts': [
            'pretty-tensor=colorize_pp_tensor.cli:main',
        ],
    },
    python_requires='>=3.6',
)
