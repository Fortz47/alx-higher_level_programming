#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list - print some basic info about Python lists
 * @p: python object pointer
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		PyObject *element = ((PyListObject *)p)->ob_item[i];

		printf("Element %zd: %s\n", i, ((element)->ob_type)->tp_name);
	}
}

/**
 * print_python_bytes - print some basic info about Python bytes objects
 * @p: python object pointer
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = ((PyVarObject *)p)->ob_size;

	printf("  size: %zd\n", size);

	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	printf("  first %d bytes:", size > 10 ? 10 : (int)size);

	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
		printf(" %02x", (unsigned char)(((PyBytesObject *)p)->ob_sval[i]));

	printf("\n");
}
