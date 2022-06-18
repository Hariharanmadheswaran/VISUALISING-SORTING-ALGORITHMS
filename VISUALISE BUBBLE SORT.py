import cv2 as cv
import numpy as np
import random as rd
import time

arr=[rd.randint(1,200) for i in range(200)]

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                return
    return
while True:
    blank=np.zeros((300,300,3),dtype="uint8")
    for i in range(len(arr)):
        line_blank=cv.line(blank,(i,300),(i,300-arr[i]),(255,255,255))
    #     blank=line_blank
    cv.imshow("BUBBLE SHORT",line_blank)
    bubble_sort(arr)
    k=+1
    if cv.waitKey(1)==ord("q"):
        cv.destroyAllWindows()
        break