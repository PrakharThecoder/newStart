
from setuptools import setup, find_packages
from typing import List
from pathlib import Path

HYPEN_E_DOT = "-e ."
ROOT_DIR = Path(__file__).parent

def get_requirements(file_path: str) -> List[str]:
    with open(ROOT_DIR / file_path, encoding="utf-8") as file:
        requirements = [
            line.strip()
            for line in file.readlines()
            if line.strip() and not line.strip().startswith("#")
        ]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="newstart",
    version="0.1.0",
    author="Prakhar",
    author_email="prakharsrivastava2005pr@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
