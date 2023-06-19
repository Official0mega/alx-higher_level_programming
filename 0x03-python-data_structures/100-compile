#!/bin/bash
PY_PATH=python3.4
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I$PY_PATH 100-print_python_list_info.c
[ $? -eq 0 ] && $PY_PATH/python ./100-test_lists.py
