/**
 * file_name: 100_print_python_list_info.c
 * Created: 13th of May, 2023.
 * Auth: David James Taiye (Official0mega).
 * Size: Undefined.
 * Project: 0x03-python-data_structures
 * Status: Submitted.
 */

#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - a C function that prints some
 * basic info about Python lists.
 * @p: Pointer
 *
 * Return: Always 0. (Success)
 */


void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
    	Py_ssize_t i;
    	PyObject *item;

    	printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    	for (i = 0; i < size; i++)
	{
        	item = PyList_GetItem(p, i);
        	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
