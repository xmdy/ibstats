#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT="$(dirname $SCRIPT_DIR)"

VENV=${ROOT}/env

if [ ! -d "$VENV" ]; then
    echo "No virtualenv, creating"
    `$SCRIPT_DIR/venv_create.sh`
    echo "Virtualenv created."
fi

source $VENV/bin/activate
cd $ROOT/src/
export PYTHONPATH=.

exec python manage.py $@