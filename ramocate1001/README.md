# ramocate
### Uses C to get memory functions. (To do some fun stuff ;] )

## Functions:
### malloc(size: int)
### calloc(size: int)
### realloc(ptr: int, newsize: int)
### free(ptr: int)

## Usage:
### malloc: Allocates memory in blocks on the heap. RETURNS: (SUCCESS: ptr: id, FAIL: "NULL")
### calloc: Allocates memory in blocks on the heap, but sets them all to zero. RETURNS: (SUCCESS: ptr: id, FAIL: "NULL")
### realloc: Englarges or shrinks allocated memory. If newsize is set to 0, it will act like free. RETURNS: (SUCCESS: ptr: id, FAIL: "NULL")
### free: Frees memory at the pointer. RETURNS (SUCCESS: none, FAIL: none)

## WARNING:
### Messing with memory is pretty dangerous and <u>WILL</u> crash and or crash other programs if not used properly.
### Best Practices:
### 1# Don't allocate too much memory (malloc, calloc)
### 2# Don't deallocate more memory than that's in a block (realloc)
### 3# Don't free memory that has not been allocated by malloc, calloc, ect. (Like py objects).
### 4# Don't free memory twice. It <u>WILL</u> crash with SIGABRT (signal abort)
### 4# Don't free random memory. <u>ESPECIALLY</u> with SIP disabled. It <u>WILL</u> crash the other process, or corrupt it!

### Also, you can find the original C library at ramocate/compiledlibs/ramocarec.c, the other ones are the compiled version of it used to comunicate python <-> c on different systems (Mac > .dylib, Linux > .so, Windows > .dll).

Rev 1: (Borne Sanders @ 7/9/25, 8:30 PM)\
Rev 2: (Borne Sanders @ 10/9/25, 10:00 PM)