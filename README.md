# test COCO api
Simplify the use of [COCO](https://github.com/cocodataset/cocoapi) to decode/encode masks and test it as an aid to developing the equivalent version of python.

## Compilation
```
gcc -c maskApi.c -o maskapi.o 
gcc -g -Wall testcocotools.c maskapi.o -o test
```
And run:
```
$ ./test
```
