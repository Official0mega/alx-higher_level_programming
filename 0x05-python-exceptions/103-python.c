/*
 * File_name: 103-python.c
 * Created: 29th May, 2023
 * Auth: David James Taiye
 * Size: undefined
 * Project: 0x05-python-exceptions
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
#define PY_SSIZE_T_C

/**
 * print_python_bytes - implementation for print python bytes function
 * @p: The Pointer to the Python list Objects.
 *
 * Return: If p is not a valid PyBytesObject, print an error message
 */
void print_python_bytes(PyObject *p)
{
	int i, bytes_len, n, error = 1;

	fflush(stdout);
	printf("[.] bytes object info\n");
	fflush(stdout);
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "bytes") == 0))
	{
		bytes_len = (int)(((PyVarObject *)p)->ob_size);
		n = bytes_len < 10 ? bytes_len : 9;
		printf("  size: %d\n", bytes_len);
		fflush(stdout);
		printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
		fflush(stdout);
		if ((n > 0) && (((PyBytesObject *)p)->ob_sval != NULL))
		{
			printf("  first %d bytes:", n + 1);
			fflush(stdout), error = 0;
			for (i = 0; i < n + 1; i++)
			{
				printf(" %02x", (unsigned char)*(((PyBytesObject *)p)->ob_sval + i));
				fflush(stdout);
			}
			printf("\n");
			fflush(stdout);
		}
	}
	if (error)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
	}
}










/**
 * print_python_float - Implementation for print python Float function
 * @p: The Pointer to the Python list Objects.
 *
 * Return: If p is not a valid PyFloatObject, print an error message
 */

void print_python_float(PyObject *p)
{
	double val;
	char *buf = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "float") == 0))
	{
		val = ((PyFloatObject *)p)->ob_fval;
		buf = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", buf);
		fflush(stdout);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
	}
}


/**
 * print_python_list - implementation for print python lists function.
 * @p: The Pointer to the Python list Objects.
 *
 * Return: If p is not a valid PyListObject, print an error message
 */

void print_python_list(PyObject *p)
{
	int i, list_len;
	PyObject *item = NULL;

	fflush(stdout);
	printf("[*] Python list info\n");
	fflush(stdout);
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "list") == 0))
	{
		list_len = (int)(((PyVarObject *)(p))->ob_size);
		printf("[*] Size of the Python List = %d\n", list_len);
		fflush(stdout);
		printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
		fflush(stdout);
		for (i = 0; (((PyListObject *)p)->ob_item != NULL) && (i < list_len); i++)
		{
			item = (PyObject *)*(((PyListObject *)p)->ob_item + i);
			printf("Element %d: %s\n", i, (item->ob_type)->tp_name);
			fflush(stdout);
			if ((item != NULL) && (item->ob_type != NULL)
				&& ((item->ob_type)->tp_name != NULL)
				&& (strcmp((item->ob_type)->tp_name, "bytes") == 0))
			{
				print_python_bytes(item);
			}
			else if ((item != NULL) && (item->ob_type != NULL)
				&& ((item->ob_type)->tp_name != NULL)
				&& (strcmp((item->ob_type)->tp_name, "float") == 0))
			{
				print_python_float(item);
			}
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
	}
}

