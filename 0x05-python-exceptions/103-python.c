#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints information about Python lists
 * @p: Pointer to the PyObject list
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;

if (!PyList_Check(p))
{
fprintf(stderr, "[ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
}

/**
 * print_python_bytes - Prints information about Python bytes
 * @p: Pointer to the PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

if (!PyBytes_Check(p))
{
fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

printf("  first %ld bytes:", (size < 10 ? size + 1 : 10));
for (i = 0; i < size && i < 10; i++)
printf(" %02x", (unsigned char)str[i]);
printf("\n");
}

/**
 * print_python_float - Prints information about Python floats
 * @p: Pointer to the PyObject float
 */
void print_python_float(PyObject *p)
{
PyObject *str;
const char *format = NULL;

if (!PyFloat_Check(p))
{
fprintf(stderr, "[ERROR] Invalid Float Object\n");
return;
}

str = PyObject_Repr(p);
format = PyUnicode_AsUTF8(str);

printf("[.] float object info\n");
printf("  value: %s\n", format);

Py_DECREF(str);
}
