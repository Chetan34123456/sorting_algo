import time
import math

#variables
gap = "          "
'''
Common documentation for functions

:param data:array
:param draw:draw the bars ,used from main file
:param speed:speed to run algorithm
:param steplistbox:show the steps
:param linkListbox: algo related links and materials
'''

def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high] # pivot element
   for j in range(low , high):
      # If current element is smaller
      if arr[j] <= pivot:
         # increment
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )

def quickSort(arr,low,high):
   if low < high:
      # index
      pi = partition(arr,low,high)
      # sort the partitions
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)

def bubble(data,draw,speed,steplistbox,linkListbox):
    '''
    :return:None
    '''
    linkListbox(f"Algorithm for Bubble Sort")
    linkListbox(gap)
    steplistbox(gap)
    steplistbox(f"Array = {data}")
    speed = int(speed)
    linkListbox("for i <- 1 to indexOfLastUnsortedElement-1")
    linkListbox(f"{gap}if leftElement > rightElement")
    linkListbox(f"{gap}{gap}swap leftElement and rightElement")

    for i in range(len(data)):
        steplistbox(" ")
        for j in range(1, len(data)-i):
            steplistbox("Comparing "+str(data[j])+ "and "+ str(data[j-1]))
            if data[j]<data[j-1]:
                steplistbox("          "+str(data[j])+" is smaller than "+str(data[j - 1])+",Hence they are swap in respective to their position")
                temp = data[j]
                data[j] = data[j-1]
                data[j-1] = temp
                draw(data, ['green' if x == j or x == j - 1
                                        else 'red' for x in range(len(data))])
                time.sleep(speed)
            elif data[j]>data[j-1]:
                draw(data, ['purple' if x == j or x == j - 1
                            else 'red' for x in range(len(data))])
                steplistbox("          "+str(data[j])+" is bigger than "+str(data[j - 1])+",Hence they remain same in respective to their position")
                time.sleep(speed)
            elif data[j]==data[j-1]:
                steplistbox("          "+str(data[j]) + " and " + str(
                    data[j - 1]) + " are equal.Hence they remain same in respective to their position")
                time.sleep(speed)

    steplistbox(gap)
    steplistbox(f"------------------------")
    steplistbox(f"Sorting Array = {data}")
    steplistbox(f"------------------------")
    steplistbox(gap)
    draw(data, ['green' for x in range(len(data))])

def selection(data,draw,speed,steplistbox,linkListbox):
    '''
    :return: None
    '''
    linkListbox(f"Algorithm for Selection Sort")
    linkListbox(gap)
    linkListbox("repeat (size - 1) times")
    linkListbox("set the first unsorted element as the minimum")
    linkListbox("for each of the unsorted elements")
    linkListbox(f"{gap}if element < currentMinimum")
    linkListbox(f"{gap}{gap}set element as new minimum")
    linkListbox(f"swap minimum with first unsorted position")

    speed = int(speed)
    for i in range(len(data)):
        index = i
        steplistbox(f"Pivot Element = {data[index]}")
        for j in range(i+1,len(data)):
            time.sleep(speed)
            steplistbox(f"{gap} Comparing pivot = {data[index]} to {data[j]}")
            draw(data, ['blue' if _ == index or _ == j else 'red' for _ in range(len(data))])
            #draw(data, ['green' if x == i else 'red' for x in range(len(data))])
            if data[index]>data[j]:
                index = j
                steplistbox(f"{gap}{gap} Pivot {data[index]} is greater than {data[j]}, thus swap the elements.")
            if data[index]==data[j]:
                steplistbox(f"{gap} Pivot {data[index]} is equal to {data[j]}, thus no change")
        data[i],data[index] = data[index],data[i]
    draw(data,["green" for _ in range(len(data))])

    steplistbox(gap)
    steplistbox(f"------------------------")
    steplistbox(f"Sorting Array = {data}")
    steplistbox(f"------------------------")
    steplistbox(gap)

def insertion(data,draw,speed,steplistbox,linkListbox):
    '''
    Move elements of arr[0..i-1], that are
    greater than key, to one position ahead
    of their current position
    :return: None
    '''
    linkListbox(f"Algorithm for Insertion Sort")
    linkListbox(gap)
    linkListbox("mark first element as sorted")
    linkListbox("for each unsorted element X")
    linkListbox(f"{gap}'extract' the element X")
    linkListbox(f"{gap}for j <- lastSortedIndex down to 0")
    linkListbox(f"{gap}{gap}if current element j > X")
    linkListbox(f"{gap}{gap}{gap}move sorted element to the right by 1")
    linkListbox(f"{gap}break loop and insert X here")

    speed = int(speed)
    for i in range(1, len(data)):
        key =data[i]
        steplistbox(f"Pivot element {key}")
        j = i - 1
        steplistbox(f"{gap}Comparing pivot {key} with {data[j]}")
        draw(data, ['green' if i == x or j == x else 'red' for x in range(len(data))])
        time.sleep(speed)
        while j >= 0 and key < data[j]:
            steplistbox(f"{gap}{gap}Pivot {key} less than {data[j]} thus shifting {key} left ")
            data[j + 1] = data[j]
            j -= 1
            draw(data, ['green' if i == x or j == x else 'red' for x in range(len(data))])
            time.sleep(1)
        data[j + 1] = key
    draw(data, ['green' for i in range(len(data))])

    steplistbox(gap)
    steplistbox(f"------------------------")
    steplistbox(f"Sorting Array = {data}")
    steplistbox(f"------------------------")
    steplistbox(gap)

def linear_search(data,searchElement, draw,speed,steplistbox,linkListbox):
    """"
    return : searchElement index
    """
    linkListbox(f"Algorithm for Linear Search")
    linkListbox(gap)
    linkListbox("for each item in the array")
    linkListbox(f"{gap}if item == value")
    linkListbox(f"{gap}{gap}return its index")

    speed,search_element = int(speed), int(searchElement)
    steplistbox(f"Search element = {search_element}")
    steplistbox(gap)

    for i in range(len(data)):
        steplistbox(f"Checking between {data[i]} and {search_element}.")
        time.sleep(speed)
        draw(data, ['blue' if _ == i else 'red' for _ in range(len(data))])
        if data[i]==search_element:
            draw(data, ['green' if _ == i else 'red' for _ in range(len(data))])
            steplistbox(gap)
            steplistbox(f"------------------------")
            steplistbox(f"Element {data[i]} is found at index {i}")
            steplistbox(f"------------------------")
            steplistbox(gap)
            return i

    steplistbox(gap)
    steplistbox(f"------------------------")
    steplistbox(f"{gap}No {search_element} in array.")
    steplistbox(f"------------------------")
    steplistbox(gap)
    return -1

def binary_search_help(data, start, end, searchElement, draw, speed, steplistbox, linkListbox):

    linkListbox(f"Algorithm for Binary Search")
    linkListbox(f"Requires Sorted array")
    linkListbox(gap)
    linkListbox(f"Compare x with the middle element.")
    linkListbox(f"If x matches with middle element, we return the mid index.")
    linkListbox(f"Else If x is greater than the mid ")
    linkListbox("   element, then x can only lie in")
    linkListbox("   right half subarray after the ")
    linkListbox("   mid element. So we recur for ")
    linkListbox("   right half.")
    linkListbox(f"Else (x is smaller) recur for the left half.")
    linkListbox(gap)
    steplistbox(f"Random array generated = {data}")
    steplistbox(f"Element to be search = {searchElement}")
    quickSort(data, 0, len(data) - 1)
    steplistbox(f"Sorted Array = {data}")
    draw(data, ['red' for x in range(len(data))])
    time.sleep(int(speed))
    return binary_search(data, start, end, searchElement, draw, speed, steplistbox, linkListbox)


def binary_search(data, start, end, searchElement, draw, speed, steplistbox, linkListbox):
    steplistbox(gap)
    if end >= start :
        mid = start + (end - start)//2
        steplistbox(f"For array {data[start:end+1]}, start index = {start} , end index = {end}")
        steplistbox(f"Middle element = {data[mid]} at index {mid} of array")


        if len(data[start:end+1]) == 2:
            steplistbox(f"{gap} {gap} New generated Arrays")
            steplistbox(f"{gap} {gap} Left array = {data[start]}")
            steplistbox(f"{gap} {gap} Right array = {data[end]}")
            draw(data, ['blue' if mid == x else 'red' for x in range(len(data))])
            time.sleep(int(speed))

        elif len(data[start:end+1]) == 1:
            draw(data, ['green' if mid == x else 'red' for x in range(len(data))])
            steplistbox(gap)
            steplistbox(f"------------------------")
            steplistbox(f"Element {data[mid]} is found at index {mid}")
            steplistbox(f"------------------------")
            steplistbox(gap)
            return int(mid)

        else:
            steplistbox(f"{gap} {gap} New generated Arrays")
            steplistbox(f"{gap} {gap} Left array = {data[start:end//2]}")
            steplistbox(f"{gap} {gap} Right array = {data[end//2:end+1]}")
            draw(data, ['blue' if mid == x else 'red' for x in range(len(data))])
            time.sleep(int(speed))


        if data[mid] == searchElement:
            steplistbox(f"Element {searchElement} found at index {mid}")
            draw(data, ['green' if mid == x else 'red' for x in range(len(data))])
            steplistbox(gap)
            steplistbox(f"------------------------")
            steplistbox(f"Element {data[mid]} is found at index {mid}")
            steplistbox(f"------------------------")
            steplistbox(gap)
            return int(mid)

        elif data[mid] > searchElement:
            draw(data, ['blue' if mid == x else 'red' for x in range(len(data))])
            time.sleep(int(speed))
            return binary_search(data, start , mid - 1, searchElement, draw, speed, steplistbox, linkListbox)

        else:
            time.sleep(int(speed))
            draw(data, ['blue' if mid == x else 'red' for x in range(len(data))])
            return binary_search(data, mid+1, end, searchElement, draw, speed, steplistbox, linkListbox)

    else:
        steplistbox(gap)
        steplistbox(f"------------------------")
        steplistbox(f"{gap}No {searchElement} in array.")
        steplistbox(f"------------------------")
        steplistbox(gap)
        return -1

def jump_search(data, searchElement, draw, speed, steplistbox, linkListbox):

    linkListbox(f"Algorithm for Jump Search")
    linkListbox(f"Requires Sorted array")
    linkListbox(gap)
    linkListbox(f"jump = square-root of lenght of array")
    linkListbox(f"If element of jump index > searching element")
    linkListbox(f"{gap}perform back linear search")
    linkListbox(gap)
    steplistbox(f"Random array generated = {data}")
    steplistbox(f"Element to be search = {searchElement}")
    quickSort(data, 0, len(data) - 1)
    steplistbox(f"Sorted array = {data}")
    steplistbox(f"Length of Array {len(data)}")
    draw(data,['red' for x in range(len(data))])
    jump = round(math.sqrt(len(data)))
    steplistbox(f"Jump = {jump}")
    steplistbox(gap)
    steplistbox(f"Initial start from Index 0")

    for i in range(jump + 1):
        draw(data, ['blue' if i * jump == x else 'red' for x in range(len(data))])
        steplistbox(f"Jump at index {i*jump}")
        time.sleep(int(speed))

        if data[i * jump] > searchElement:
            steplistbox(gap)
            steplistbox(f"Element(to be find) {searchElement} is less than {data[i* jump]}")
            steplistbox(f"Backward search from {data[(i)*jump]} to {data[(i-1)*jump]}")

            for j in range(jump):
                draw(data, ['blue' if i * jump - j  == x else 'red' for x in range(len(data))])
                time.sleep(int(speed))

                if data[i * jump - j] == searchElement:
                    draw(data, ['green' if i * jump - j  == x else 'red' for x in range(len(data))])
                    steplistbox(f"Element(searching element) {searchElement} found at index {i*jump-j}")
                    return int(i * jump - j)

                elif data[i * jump - j] != searchElement:
                    steplistbox(f"{gap}Shifting one index back at index {i * jump - j}")
            steplistbox(f" No {searchElement}  in array")
            return int(-1)

        elif data[i * jump] == searchElement:
            draw(data, ['green' if i* jump == x else 'red' for x in range(len(data))])
            steplistbox(f"Element(to be find) {searchElement} found at index {i * jump}")
            return int(i * jump)

    for i in range(jump - 1 * jump, len(data)):
        draw(data, ['blue' if jump - i  == x else 'red' for x in range(len(data))])
        time.sleep(int(speed))
        if data[i] == searchElement:
            draw(data, ['green' if i == x else 'red' for x in range(len(data))])
            steplistbox(f"Element(to be find) {searchElement} found at index {i}")
            return int(i)
