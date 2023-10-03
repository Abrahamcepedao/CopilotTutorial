# create a functions that receives two arrays and returns a sorted array with the elements from both arrays

def merge(arr1, arr2):
    #create a new array
    merged = []
    #while both arrays still have elements
    while len(arr1) > 0 and len(arr2) > 0:
        #if the first element of the first array is less than the first element of the second array
        if arr1[0] < arr2[0]:
            #add the first element of the first array to the merged array
            merged.append(arr1[0])
            #remove the first element from the first array
            arr1.pop(0)
        #else the first element of the second array is less than the first element of the first array
        else:
            #add the first element of the second array to the merged array
            merged.append(arr2[0])
            #remove the first element from the second array
            arr2.pop(0)
    #add the remaining elements of the first array to the merged array
    merged.extend(arr1)
    #add the remaining elements of the second array to the merged array
    merged.extend(arr2)
    #return the merged array
    return merged

print(merge([1, 3, 5, 7], [2, 4, 6, 8]))