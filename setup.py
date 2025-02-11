import setuptools

with open("README.md",'r',encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Wine_Quality_Classification"
AUTHOR_USER_NAME = "prodip1023"
SRC_REPO = "wineClass"
AUTHOR_EMAIL = "prodip1023@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A machine learning project to classify wine quality based on features like fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker " : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    
)