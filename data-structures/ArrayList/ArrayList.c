/*
 * start Date : 12.09.2017
 * desc : It's list used array
 */

#include <stdio.h>
#include "ArrayList.h"

void ListInit(List *plist)
{
	plist->numOfData = 0;
	plist->curPosition = -1;
}

void LInsert(List *plist, LData data)
{
	plist->arr[(plist->numOfData)++] = data;
	plist->curPosition += plist->numOfData;
}

int LCount(List *plist)
{
	return plist->numOfData;
}

int LFirst(List *plist, LData *pdata)
{

	if(plist->numOfData == 0)
		return FALSE;

	plist->curPosition = 0;

	*pdata = plist->arr[(plist->curPosition)++]; 

	return TRUE;

}

int LNext(List *plist, LData *pdata)
{
	if(plist->curPosition < plist->numOfData){
		
		*pdata = plist->arr[(plist->curPosition)++];

		return TRUE;

	}else{
		return FALSE;

	}
}

LData LRemove(List *plist)
{

	LData num = plist->arr[plist->curPosition];

	while(1)
	{
		plist->arr[(plist->curPosition)] = plist->arr[(plist->curPosition)+1];

		plist->curPosition++;

		if(plist->curPosition < plist->numOfData)
		{
			plist->numOfData--;
			return num;
		}
	}
}
