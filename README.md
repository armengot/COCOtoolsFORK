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

# Encoding/Decoding with standar API
In the main function there is an example.
After header includes ...
```
#include "maskApi.h"
```
... and some functions (see the code) ... you can find the main():
```
int main()
{   
    char* output;
    byte mout[H*W];
    byte **outmask=NULL;  
    byte **dmask;
    byte *mravel;
    
    /* ORIGINAL HxW ARRAY */
    dmask = fillmask(mask,H,W);
    printf("ORIGINAL ARRAY\n");
    arrayprint(dmask,H,W);

    /* Coco Ravel() style */
    mravel = ravel(mask,H,W);

    /* RLE <== mask[rows][cols] */
    rleEncode(&encodedmask,mravel,W,H,1);    

    /* RLE->cnts ==> string */
    output = rleToString(&encodedmask);    
    printf("RLE:\n");    
    printf("%s\n",output);
          
    /* test string ==> RLE->cnts */
    printf("\nDECODE:\n");
    rleFrString(&decodedmask,output,H,W);
    free(output);

    /* RLE->cnts ==> string */
    rleDecode(&decodedmask,mout,1);    
    printf("\n:%d:%d:%d\n",mout[0],mout[1],mout[5]);

    /* test reshape ==> Array2d[Rows][Cols] */
    outmask = reshape(mout,H,W);     
    arrayprint(outmask,H,W);

    freemat(outmask,H);    
    freemat(dmask,H);      
    rleFree(&encodedmask);
    rleFree(&decodedmask);
    return(0);
}
```
The two functions in the API:
```
    rleFrString(&decodedmask,output,H,W);
    rleDecode(&decodedmask,mout,1);  
```
Are traslated to Python in a one only funcion. See the Python folder.

## Speed
C standard function is faster than the equivalent in Python :(
