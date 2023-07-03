#include <Python.h>

/**
 * print_python_string - Prints information about Python string objects
 * @p: PyObject string object
 */
void print_python_string(PyObject *p)
{
Py_ssize_t length;
Py_UNICODE *value;
int kind;

printf("[.] string object info\n");

if (!PyUnicode_Check(p))
{
printf("  [ERROR] Invalid String Object\n");
return;
}

length = PyUnicode_GET_LENGTH(p);
value = PyUnicode_AS_UNICODE(p);
kind = PyUnicode_KIND(p);

printf("  type: compact ");

if (kind == PyUnicode_1BYTE_KIND)
printf("ascii\n");
else if (kind == PyUnicode_2BYTE_KIND)
printf("unicode object\n");
else if (kind == PyUnicode_4BYTE_KIND)
printf("wide unicode object\n");
else
{
printf("[ERROR] Unknown kind of Unicode object\n");
return;
}

printf("  length: %ld\n", length);
printf("  value: %ls\n", value);
}
