#include <stdlib.h>

int* cMalloc(int size) {
    return (int*)malloc(size * sizeof(int));
}

int* cCalloc(int size) {
    return (int*)calloc(size, sizeof(int));
}

int* cRealloc(int* ptr, int new_size) {
    return (int*)realloc(ptr, new_size * sizeof(int));
}

void cFree(int* ptr) {
    free(ptr);
}
