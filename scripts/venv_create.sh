#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT="$(dirname $SCRIPT_DIR)"

VENV=${ROOT}/env
rm -rf ${VENV}
virtualenv ${VENV}
source $VENV/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools
pip --no-cache-dir install -r requirements.txt