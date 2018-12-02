# coding: "utf-8"

from setuptools import setup, find_packages

#setup(name='guestbook')

setup(
    name="guestbook",  # 程序包的名称
    version='1.0.0',   # 程序的版本号
    packages=find_packages(),  # 指定所有捆绑的程序包
    include_package_data=True,   # 指定是否安装除.py之外的程序包资源
    install_requires=[
        'Flask',       # 列表指定依赖包，一般不指定版本
    ],
    entry_points="""
        [console_scripts]
        guestbook = guestbook:main
    """,
)



