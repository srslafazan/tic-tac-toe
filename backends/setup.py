from setuptools import setup

setup(
    name="api",
    title="Tic Tac Toe API",
    version="1.0.0",
    author="Shain Lafazan",
    author_email="shain.codes@gmail.com",
    description="Game Engine API for Tic Tac Toe",
    url="https://github.com/srslafazan/tic-tac-toe.git",
    license="MIT",
    packages=["api"],
    install_requires=["flask==2.3.2", "flask_cors==3.0.10", "flasgger==0.9.7.1"],
)
