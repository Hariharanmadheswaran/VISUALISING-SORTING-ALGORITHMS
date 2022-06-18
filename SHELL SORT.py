import cv2 as cv
import numpy as np
import random as rd
import time

arr=[rd.randint(1,200) for i in range(200)]


def shell_sort(arr, gap, i):
    pivot = arr[i]
    j = i - gap
    while j >= 0 and pivot < arr[j]:  # < -- indicates for ascending order
        arr[j + gap] = arr[j]
        j -= gap
    arr[j + gap] = pivot
    #             return arr
    return
gap=len(arr)//2
ss=[*range(gap,len(arr),gap)]
# print(ss)
index=0
while True:
    blank=np.zeros((600,600,3),dtype="uint8")
    for i in range(len(arr)):
        line_blank=cv.line(blank,(i,600),(i,600-arr[i]),(255,255,255))
    #     blank=line_blank
    cv.imshow("SHELL SHORT",line_blank)
    if index<len(ss):
        shell_sort(arr,gap,ss[index])
        index+=1
    else:
        gap=gap//2
        if gap==0:
            break
        ss=[*range(gap,len(arr),gap)]
        index=0
    time.sleep(.1)
#     print(arr)
    if cv.waitKey(1)==ord("q"):
        cv.destroyAllWindows()
        break 