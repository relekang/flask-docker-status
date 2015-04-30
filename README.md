# flask-docker-status [![Build status](https://ci.frigg.io/badges/relekang/flask-docker-status/)](https://ci.frigg.io/relekang/flask-docker-status/last/) [![Coverage status](https://ci.frigg.io/badges/coverage/relekang/flask-docker-status/)](https://ci.frigg.io/relekang/flask-docker-status/last/)
A simple flask project that displays docker ps. It is probably wise to run this behind
some sort of authentication.

## Example output
```
CONTAINER ID        IMAGE                          COMMAND             CREATED             STATUS              PORTS               NAMES
bf6eeb9b8d2b        relekang/relekang-test-base:latest   "/bin/sleep 3600"   9 seconds ago       Up 9 seconds                            dyn-0e995327-40ab-4137-8f3e-4fdfe03da6f9
```
