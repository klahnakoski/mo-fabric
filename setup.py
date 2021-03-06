# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from __future__ import unicode_literals
from setuptools import setup
setup(
    description=u'Thin facade atop fabric',
    license=u'MPL 2.0',
    author=u'Kyle Lahnakoski',
    author_email=u'kyle@lahnakoski.com',
    long_description_content_type=u'text/markdown',
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 2.7","Programming Language :: Python :: 3.7","Development Status :: 4 - Beta","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)"],
    install_requires=["fabric2","invoke","mo-dots>=3.22.19344","mo-files>=3.26.19346","mo-future>=3.17.19324","mo-kwargs>=3.20.19344","mo-logs>=3.21.19344","mo-math>=3.28.19346"],
    version=u'3.30.19346',
    url=u'https://github.com/klahnakoski/mo-fabric',
    python_requires=u'==2.7, >=3.6',
    zip_safe=False,
    packages=["mo_fabric"],
    long_description=u'# mo-fabric\n\nA fa\xe7ade atop [fabric2](http://www.fabfile.org/)\n\n## Overview\n\nI have revisited [Fabric](http://www.fabfile.org/) (September 2018) to find it can handle multiple threads and multiple connections!  This is great news: it makes all my automation faster!\n\nLike with most APIs, I made a fa\xe7ade because Fabric is not congruent to my own programming conventions. This is not bad, just different: The domain I work in is slightly different than what the Fabric developers expect. \n\nHere are the differences:\n\n* All `stdout` and `strerr` from the remote machine is annotated, and shunted, to the local logging module.\n* A few convenience methods are added:\n  * `conn.exists(path)` - to test if a remote file exists\n  * `with conn.warn_only():` - context manager if you do not care if your commands fail\n  * `get(remote, local, use_sudo=False)` - allows you to use tilde (`~`) on Windows to refer to home directory\n  * `put(local, remote, use_sudo=False)` - similar to `get`, except copies files to remote\n  * `sudo(command)` works with the `cd()` context manager\n  * `Result.__contains__()` so checking for patterns in command output is simpler:\n    ```python\n        result = conn.run("ls /data1", warn=True)\n        not_found = "No` such file or directory" in result\n    ```\n',
    name=u'mo-fabric'
)