# Installation

Install from project root directory.

* Install Poetry if not already done:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

* Export necessary environment variables. You only need to do this for the current shell session.
```bash
export LD_LIBRARY_PATH=${PWD}/data/mujoco210/bin:/usr/lib/nvidia
export MUJOCO_PY_MUJOCO_PATH=${PWD}/data/mujoco210
```

* Install
```bash
poetry install
```