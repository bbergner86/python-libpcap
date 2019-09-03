# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages
# from pkg_resources import resource_string
from setuptools import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext


url = "https://github.com/caizhengxin/python-libpcap"


ext_modules = [
    Extension(
        "*",
        sources=["{}/{}".format(directory, file)],
        libraries=["m"],
        # include_dirs=["src"],
        # extra_compile_args=[],
        # extra_link_args=[],
    )
    for directory, dirs, files in os.walk("pylibpcap")
    for file in files if ".pyx" in file
]


setup(
    name="python-libpcap",
    version="0.1.0",
    author="JanKinCai",
    author_email="jankincai12@gmail.com",
    maintainer="JanKinCai",
    maintainer_email="jankincai12@gmail.com",
    url=url,
    download_url=url + ".git",
    license="BSD",
    description="Cython libpcap",
    long_description="Cython libpcap",
    keywords=[
        "python-libpcap",
        "pylibpcap",
    ],
    zip_safe=False,
    packages=find_packages(),

    cmdclass={
        "build_ext": build_ext
    },
    ext_modules=cythonize(ext_modules),

    install_requires=[
    ],

    entry_points={
        "console_scripts": [
            "pylibpcap = pylibpcap.command:main",
        ],
        # "gui_scripts": [
        # ],
    },

    # package_data={
    #     "": ["*.txt"],
    # },
    include_package_data=True,  # MANIFEST.in
    # exclude_packet_data=[],
    # data_files=[],
    # scripts=["xxx.py"],

    # package_dir=[],
    # requires=[],
    # provides=[],

    setup_requires=[
        "setuptools",
        "Cython",
    ],

    # project_urls = {
    #     "Documentation": "",
    #     "Source Code": "",
    # },

    # dependency_links=[],
    # extras_require=[],

    platforms="any",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD License',
    ],
)