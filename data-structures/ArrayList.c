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

