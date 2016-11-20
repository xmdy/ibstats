#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT="$(dirname $SCRIPT_DIR)"

VENV=${ROOT}/env
source $VENV/bin/activate
cd $ROOT/src/
export PYTHONPATH=.

exec python $@