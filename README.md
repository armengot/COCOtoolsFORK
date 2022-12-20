# test COCO api
Simplify COCO usage and test it for developing python equivalent version.

## Compilation
```
gcc -c maskApi.c -o maskapi.o 
gcc -g -Wall testcocotools.c maskapi.o -o test
```
And run:
```
$ ./test
```
