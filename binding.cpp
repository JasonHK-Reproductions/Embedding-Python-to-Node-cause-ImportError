#define NAPI_VERSION 4
#include <napi.h>

#define PY_SSIZE_T_CLEAN
#include <Python.h>

class ConstructorDestructor
{
    public:
        ConstructorDestructor();
        ~ConstructorDestructor();
};

ConstructorDestructor::ConstructorDestructor()
{
    Py_Initialize();
}

ConstructorDestructor::~ConstructorDestructor()
{
    Py_Finalize();
}

static ConstructorDestructor constructor_destructor;

Napi::Object Init(Napi::Env env, Napi::Object exports)
{
    Py_XDECREF(PyImport_ImportModule("ctypes"));
    
    if (PyErr_Occurred())
    {
        PyErr_Print();
        exit(1);
    }

    return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init);
