# test COCO api
Simplify [COCO](https://github.com/cocodataset/cocoapi) usage to decode/encode masks and test it to help in developing tasks of python equivalent version.

## Compilation
```
gcc -c maskApi.c -o maskapi.o 
gcc -g -Wall testcocotools.c maskapi.o -o test
```
And run:
```
$ ./test
```
