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

int GetRChildIDX(int idx)
{
	return GetLChildIDX(idx)+1;
}

int GetHiPriChildIDX(Heap *ph, int idx)
{
	if(GetLChildIDX(idx) > ph->numOfData)
	{	
		return 0;
	}
	else if (GetLChildIDX(idx) == ph->numOfData)
	{
		return GetLChildIDX(idx);
	}
	else
	{
		if(ph->heapArr[GetLChildIDX(idx)].pr > ph->heapArr[GetRChildIDX(idx)].pr)
			return GetRChildIDX(idx);
		else
			return GetLChildIDX(idx);
	}
}

//Insert data
void HInsert(Heap *ph, HData data, Priority pr)
{
	int idx = ph->numOfData+1;
	HeapElem nelm = {pr, data};

	while(idx != 1)
	{
		if(pr < (ph->heapArr[GetParentIDX(idx)].pr))
		{
			ph->heapArr[idx] = ph->heapArr[GetParentIDX(idx)];
			idx = GetParentIDX(idx);
		}
		else
		{
			break;
		}
	}

	ph->heapArr[idx] = nelm;
	ph->numOfData += 1;
}

//Delete First data
HData HDelete(Heap *ph)
{
	HData retData = (ph->heapArr[1]).data;
	HeapElem lastElem = ph->heapArr[ph->numOfData];

	int parentIdx = 1;
	int childIdx;

	while(childIdx = GetHiPriChildIDX(ph, parentIdx))
	{
		if(lastElem.pr <= ph->heapArr[childIdx].pr)
			break;

		ph->heapArr[parentIdx] = ph->heapArr[childIdx];
		parentIdx = childIdx;
	}

	ph->heapArr[parentIdx] = lastElem;
	ph->numOfData -= 1;

	return retData;
}
