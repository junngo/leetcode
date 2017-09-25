#include <stdio.h>
#include <stdlib.h>
#include "ArrayBaseStack.h"

void StackInit(Stack *pstack)
{
	pstack->topIndex = -1;
}

int SIsEmpty(Stack *pstack)
{
	if(pstack->topIndex == -1)
		return TRUE;
	else
		return FALSE;
}

void SPush(Stack *pstack, Data data)
{
	pstack->topIndex += 1;
	pstack->stackArr[pstack->topIndex] = data;
}

Data SPop(Stack *pstack)
{
	int tempIdx;
	
	if(SIsEmpty(pstack))
	{
		printf("Memory Error\n");
		exit(-1);
	}

	tempIdx = pstack->topIndex;
	
//	pstack->stackArr[(pstack->topIndex)-1] = pstack->stackArr[pstack->topIndex];
//	error code.. fault memory when index is 0
	
	pstack->topIndex -= 1;

	return pstack->stackArr[tempIdx];
}

Data SPeek(Stack *pstack)
{

	if(SIsEmpty(pstack))
	{
		printf("Memory Error\n");
		exit(-1);
	}
	
	return pstack->stackArr[pstack->topIndex];

}
