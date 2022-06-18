import cv2 as cv
import numpy as np
import random as rd
import time
arr=[rd.randint(1,200) for i in range(400)]
having=[(0,len(arr)-1)]

def quick_sort(arr,left,right):
    pivot=left
    left=left+1
    end=right
    while left<right:
        while arr[left]<=arr[pivot] and left<right:
            left+=1
#         print(left)
        while arr[right]>=arr[pivot] and right>0:
            right-=1
#         print(right)
        if left<right:
            arr[left],arr[right]=arr[right],arr[left]
    if arr[right]<arr[pivot]:
        arr[pivot],arr[right]=arr[right],arr[pivot]
    return pivot,right,end


def repeatea():
    global having, arr
    while having != []:
        if having[-1][0] < having[-1][1]:
            #             print(having[-1][0],having[-1][1],end="  ")
            x, y, z = quick_sort(arr, having[-1][0], having[-1][1])
            #             print(having,end="   ")
            #             print(arr)
            having.pop(-1)
            #             print(having)

            having.append((x, y - 1))
            having.append((y + 1, z))
        #             print(having)
        else:
            having.pop(-1)
        break


while True:
    blank = np.zeros((300, 300, 3), dtype="uint8")
    repeatea()
    print(arr)
    for i in range(len(arr)):
        line_blank = cv.line(blank, (i, 300), (i, 300 - arr[i]), (255, 255, 255))
    #     blank=line_blank
    cv.imshow("QUICK SHORT", line_blank)

    # time.sleep(.1)
    #     print(arr)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break