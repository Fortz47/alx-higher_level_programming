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
	printf("[*] Size of the Python List = %zu\n", PyList_Size(p));
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); i++)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
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

	Py_ssize_t size = PyBytes_GET_SIZE(p);

	printf("  size: %zd\n", size);

	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %d bytes:", size > 10 ? 10 : (int)size);

	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
		printf(" %02x", (unsigned char)PyBytes_AsString(p)[i]);

	printf("\n");
}
