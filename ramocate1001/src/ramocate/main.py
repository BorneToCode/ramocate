import ctypes
import os
import platform

setPath = os.path.join(os.path.dirname(__file__), 'compiledlibs')

def _gCL():
    if platform.system() == 'Darwin':
        return os.path.abspath(os.path.join(setPath, 'ramocatedylib.dylib'))
    elif platform.system() == 'Linux':
        return os.path.abspath(os.path.join(setPath, 'ramocateso.so'))
    else:
        return os.path.abspath(os.path.join(setPath, 'ramocatedll.dll'))


_lib = ctypes.CDLL(_gCL())

_lib.cMalloc.argtypes = [ctypes.c_int]
_lib.cMalloc.restype = ctypes.POINTER(ctypes.c_int)

_lib.cCalloc.argtypes = [ctypes.c_int]
_lib.cCalloc.restype = ctypes.POINTER(ctypes.c_int)

_lib.cRealloc.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
_lib.cRealloc.restype = ctypes.POINTER(ctypes.c_int)

_lib.cFree.argtypes = [ctypes.POINTER(ctypes.c_int)]
_lib.cFree.restype = None

def malloc(size):
    return _lib.cMalloc(size)

def calloc(size):
    return _lib.cCalloc(size)

def realloc(ptr, newsize):
    return _lib.cRealloc(ptr, newsize)

def free(ptr):
    _lib.cFree(ptr)
