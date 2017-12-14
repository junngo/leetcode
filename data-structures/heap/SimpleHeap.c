#include "SimpleHeap.h"

void HeapInit(Heap *ph)
{
	ph->numOfData = 0;
}

int HIsEmpty(Heap *ph)
{
	if(ph->numOfData == 0)
		return TRUE;
	else
		return FALSE;
}

/*
 * Left child node index  : parent node idx * 2
 * right child node indxe : parent node idx * 2 +1
 * parent node idx : child node / 2
 */

int GetParentIDX(int idx)
{
	return idx/2;
}

int GetLChildIDX(int idx)
{
	return idx*2;
}

int GetRChildIdx(int idx)
{
	return GetLChildIDX(idx)+1;
}
