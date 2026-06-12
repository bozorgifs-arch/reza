#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Nobitex AI Scalper Pro
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nobitex-ai-scalper",
    version="1.0.0",
    author="Reza",
    author_email="reza@nobitex.ir",
    description="سیستم معاملاتی هوشمند خودمختار برای صرافی نوبیتکس",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bozorgifs-arch/reza",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "pandas>=1.5.0",
        "python-dotenv>=0.20.0",
        "pyperclip>=1.8.2",
        "pyttsx3>=2.90",
        "pyinstaller>=5.0.0",
    ],
)