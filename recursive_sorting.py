# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i= 0
    j=0
    k=0
    for k in range(0,len(merged_arr)):
        # print(k)
        if (i < len(arrA)) and (len(arrA)>0)and (len(arrB) > 0) and (j < len(arrB)) and arrA[i] < arrB[j]: 
            merged_arr[k] = arrA[i]
            i += 1
            k += 1
            # print(i)
            # print(k)
            # print(merged_arr)
        elif (j < len(arrB)) and (len(arrB) > 0)and (len(arrA)>0) and (i < len(arrA))  and arrA[i] > arrB[j]:
            merged_arr[k] = arrB[j]
            j += 1
            k += 1
            # print(k)

        elif (j < len(arrB)) and (len(arrB) > 0) and (i == len(arrA)):
            merged_arr[k] = arrB[j]
            j+=1
            # print(k)

        elif (i < len(arrA)) and (len(arrA)>0) and (j == len(arrB)):
            merged_arr[k] =  arrA[i]
            i += 1
            # print(k)


    return merged_arr

arr = merge([50,1,3], [6,2,88])

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):


    if len(arr)> 1:
        datasubset_1 = arr[0:int((len(arr)/2))] #start to half
        datasubset_2 = arr[int((len(arr)/2)):] #half to end
        data1 = merge_sort(datasubset_1)
        data2 = merge_sort(datasubset_2)   

        if len(data1) >= 1 and len(data2) >= 1:
            arr = merge(data1, data2)
        
    
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr







            # if datasubset_1[0] < datasubset_2[0]:
        #     arr1 = [datasubset_1[0]]
        #     arr2 = datasubset_1[1:]

        #     merge_sort(arr2)
        #     arr3 = datasubset_2
        #     merge_sort(arr3)
        #     arr = arr1 + arr2 + arr3
        # else:
        #     arr1 = [datasubset_2[0]]
        #     arr2 = datasubset_1
        #     merge_sort(arr2)
        #     arr3 = datasubset_2[1:]
        #     merge_sort(arr3)
        #     arr = arr1 + arr2 + arr3




        # if datasubset_1[0] < datasubset_2[0]:
        #     datasubset_1.pop(datasubset_1[0])
        #     arr = [datasubset_1[0]]
        #     if datasubset_1[0] < datasubset_2[0]:
        #         datasubset_1.pop(datasubset_1[0])
        #         arr = arr + [datasubset_1[0]]
            
        #     else:
        #         arr = arr + [datasubset_2[0]]
        # else:
        #     datasubset_2.pop(datasubset_2[0])
        #     arr = [datasubset_2[0]]