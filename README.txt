Dockerized Homework assignment template
=======================================

This is a template for doing various interview homework
assignments without having a proper development environment set
up on my machine.  Everything is dockerized and I use vscode so all
I need to do to work on the code is docker-desktop and vscode installed.

Development
-----------

This homework is using Docker, and is meant to be developed using
vscode devcontainer. Follow instructions in:

https://code.visualstudio.com/docs/remote/containers

to get your vscode set up, and then follow the existing container
quickstart to get going:

https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container

Testing and running outside of vscode
-------------------------------------

If all you want is to build the container, run tests and run the
application a Makefile is provided.

```
make build test run
```

Should run all the  tests and set you up with an instance listening on:

http://localhost:6544
