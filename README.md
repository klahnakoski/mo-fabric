# mo-fabric

A façade atop [fabric](http://www.fabfile.org/)

## Overview

I have revisited [Fabric](http://www.fabfile.org/) (September 2018) to find it can handle multiple threads and multiple connections. This makes all my automation faster!

Like with most APIs, I made a façade because Fabric is not congruent to my own programming conventions. This is not bad, just different: The domain I work in is slightly different than what the Fabric developers expect. 

Here are the differences:

* All `stdout` and `strerr` from the remote machine is annotated, and shunted, the the local logging module.
* A few convenience methods are added:
  * `conn.exists(path)` - to test if a remote file exists
  * `with conn.warn_only():` - context manager if you do not care if your commands fail
  * `get(remote, local, use_sudo=False)` - allows you to use tilde (`~`) on Windows to refer to home directory
  * `put(local, remote, use_sudo=False)` - similar to `get`, except copies files to remote
  * `sudo(command)` works with the `cd()` context manager
* Added `Result.__contains__()` so checking for patterns in command output is simpler:
  ```python
    not_found = "No` such file or directory" in result
  ```
