
def sort(arr):
    if arr[1] > arr[0]:
        highest = arr[1]
        s_highest = arr[0]
    else:
        highest = arr[0]
        s_highest = arr[1]

    for i in range(len(arr)-2):
        print(arr[i+2]) 
        # print(s_highest)
        # print(highest)
        if i == 1 or i == 0: 
            continue
        # if arr[i + 2] > s_highest and arr[i + 2] < highest:
        #     s_highest = arr[i + 2]
        if (arr[i + 2] > highest):
            print("here")
            s_highest = highest
            highest = arr[i + 2]
        elif (arr[i+2] > s_highest):
            print("here")
            s_highest = arr[i + 2]
        else: 
            continue        
    return s_highest


def main(): 
  array = [1,2,3,4,5]
  print(sort(array))


if __name__ == "__main__": 
  main()
