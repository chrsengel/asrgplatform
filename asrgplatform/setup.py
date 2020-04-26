from setuptools import setup

setup(
    name="asrgplatform",
    packages=["asrgplatform"],
    include_package_data=True,
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "flask-login"
    ],
)
