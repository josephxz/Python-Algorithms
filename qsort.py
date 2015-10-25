'''
function partition(lst, lo, hi)
function qsort(lst, lo, hi)
'''

def qsort(lst, lo, hi):
    if hi-lo <=0:
        return;
    middle = partition(lst, lo, hi);
    qsort(lst, lo, middle-1);
    qsort(lst, middle+1, hi);
    

def partition(lst, lo, hi):
    pivot = hi;
    i = lo;
    j = hi;
    while i<j:
        while i<hi and lst[i] <= lst[pivot]:
            i+=1;
        while j>lo and lst[j] >= lst[pivot]:
            j-=1;
        if i < j:
            temp = lst[i];
            lst[i] = lst[j];
            lst[j] = temp;
            
    temp = lst[i];
    lst[i] = lst[pivot];
    lst[pivot] = temp;
    return i;