#!/usr/bin/env python3
from .models import List

def ShowLists():
    allItems = List.objects.all()
    mList = []
    for i in allItems:
        mList.append(i)
    
    return mList

def AddItem(item, checked = False):
    temp = List()
    temp.item = item
    temp.checked = checked
    temp.save()