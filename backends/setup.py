from setuptools import setup

setup(
    name="api",
    version="1.0.0",
    author="Shain Lafazan",
    author_email="shain.codes@gmail.com",
    description="API for Tic Tac Toe",
    url="https://github.com/srslafazan/tic-tac-toe.git",
    license="MIT",
    packages=["api"],
    install_requires=[
        "Flask == 2.3.2",
    ],
)
