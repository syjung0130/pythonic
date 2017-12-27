작성한 프로그램을 사용자를 위해 release를 하거나 협업을 위해 패키지(라이브러리)로 제공해야할 때가 있다.

release를 하기 위해서는 사용자가 실행하기 위해 실행파일을 생성해야한다.

그리고 다른 개발자가 패키지를 import해서 사용하기 위해서는 package 로 설치를 해주어야 한다.

우선 작성한 코드를 package로 설치하는 방법을 보자.



1. 프로젝트 구조
==============
일단 작성법을 확인하기 위해 예제를 간단하게 작성해서 확인해보자.

프로젝트의 디렉터리 구조는 다음과 같다.

###########################################

HowToPackage/
README.txt
setup.py
HelloWorld/
__init__.py

Hello.py

World.py

###########################################



2. setup.py 작성
=============
setup.py는 다음과 같이 작성했다.
###########################################
from distutils.core import setup

setup(
name='HowToPackage',
version='0.1dev',
packages=['HelloWorld',],
license='sy',
long_description=open('README.txt').read(),
)
###########################################




name은 만약 PyPI(Python Package Index)에 패키지로 등록할 것이라면 중복되지 않도록 unique해야 한다.

version은 version정보,

package는 내가 넣은 Python sourece code의 위치에 대한 정보이다.



자세한 내용은 다음을 참조.

( http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html )

( http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html )
######################################################################################
However, there are only three required fields: name, version, and packages. The name field must be unique if you wish to publish your package on the Python Package Index (PyPI). The version field keeps track of different releases of the project. The packages field describes where you’ve put the Python source code within your project.
######################################################################################


3. Python source code 작성
======================
HellowWorld 디렉터리 안에 작성한 코드들이 포함되어 있는데,
내용은 다음과 같다.
[ __init__.py ]
###########################################
__all__ = ['Hello', 'World']

###########################################





[ Hello.py]
###########################################
1
2
def hello():
print("Hello")
cs
###########################################



[ World.py ]
###########################################
1
2
def world():
print("World~")
cs
###########################################



4. 패키지 설치
=================

다음명령을 실행하면 작성한 패키지가 설치된다.

~ HowToPackage $ python setup.py install

running install

running build

running build_py

running install_lib

running install_egg_info

Removing /usr/local/lib/python2.7/site-packages/HowToPackage-0.1dev-py2.7.egg-info

Writing /usr/local/lib/python2.7/site-packages/HowToPackage-0.1dev-py2.7.egg-info



설치한 패키지 동작 확인

sy:~ sy$ python

Python 2.7.13 (default, Apr  4 2017, 08:47:57)

[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin

Type "help", "copyright", "credits" or "license" for more information.

>>> from HelloWorld import *

>>> Hello.hello()

Hello

>>> World.world()

World~





다음에는 바이너리(실행파일)로 설치하는 방법을 알아보자..

https://docs.python.org/3/distutils/builtdist.html

https://docs.python.org/3/distutils/setupscript.html



https://devgrapher.com/?p=827

http://www.aosabook.org/en/packaging.html



