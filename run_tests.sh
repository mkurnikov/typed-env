#!/usr/bin/env bash

set -e
set -x

/code/mkurnikov/.virtualenvs/typed-env2/bin/nose2 -v
/code/mkurnikov/.virtualenvs/typed-env/bin/nose2 -v