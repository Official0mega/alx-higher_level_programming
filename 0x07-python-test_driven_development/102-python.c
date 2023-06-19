/*
 * File_name: 102-python.c
 * Created: 2nd June, 2023
 * Auth: David James Taiye
 * Size: undefined
 * Project: 0x07-python-test_driven_development
 * Status: submitted.
 */

#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <float.h>
#include <sys/types.h>
#include <python3.4/Python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>
#include <python3.4/floatobject.h>
#include <python3.4/unicodeobject.h>
#define PY_SSIZE_T_C
#define PY_SSIZE_T_CLEAN

/**
 * print_python_string - implementation for print python bytes function
 * @p: The Pointer to the Python string
 *
 * Return: If p is not a valid PyBytesObject, print an error message
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t str_len;
	Py_UNICODE *str = NULL;
	char *fmt_str = "  value: %ls\n";

	fflush(stdout);
	printf("[.] string object info\n");
	fflush(stdout);
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "str") == 0))
	{
		str = PyUnicode_AsWideCharString(p, &str_len);
		printf("  type: %s%s\n",
			   ((PyASCIIObject *)p)->state.compact ? "compact " : "",
			   ((PyASCIIObject *)p)->state.ascii ? "ascii" : "unicode object");
		fflush(stdout);
		printf("  length: %d\n", (int)str_len);
		fflush(stdout);
		printf(fmt_str, str);
		fflush(stdout);
		PyMem_Free(str);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
		fflush(stdout);
	}
}
