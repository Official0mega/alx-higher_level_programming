/*
 * File_name: 103-python.c
 * Created: 17th May, 2023
 * Auth: David James Taiye
 * Size: undefined
 * Project: 0x04-python-more_data_structures
 * Status: submitted.
 */

#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - A function that gives data of the PyBytesObject
 *
 * @p: the PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, obj_size = 0;
	char *string = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &string, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
		while (obj_size < size + 1 && obj_size < 10)
		{
			printf(" %02hhx", string[obj_size]);
			obj_size++;
		}
		printf("\n");
	}
}

/**
 * print_python_list - A function that gives data of the PyListObject
 *
 * @p: the PyObject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int obj_size = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (obj_size < size)
		{
			item = PyList_GET_ITEM(p, obj_size);
			printf("Element %d: %s\n", obj_size, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			obj_size++;
		}
	}
}
