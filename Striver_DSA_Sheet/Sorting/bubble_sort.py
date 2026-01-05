def bubble_sort(arr):
    n = len(arr)  # Array length store chestunnam

    # Outer loop -> number of passes
    # Maximum n-1 passes avasaram
    for i in range(n):
        
        swapped = False  
        # swapped flag -> ee pass lo swap jariginda leda ani check cheyadaniki
        # Optimization kosam (already sorted ayite early stop)

        # Inner loop -> adjacent elements ni compare chestam
        # n - i - 1 enduku ante:
        # Last i elements already sorted kabatti compare cheyyalsina avasaram ledu
        for j in range(0, n - i - 1):

            # ASCENDING ORDER LOGIC
            # Left element right element kanna pedda ayite -> swap
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

            # ---------------------------------------------
            # DESCENDING ORDER LOGIC (ONLY CHANGE THIS LINE)
            # if arr[j] < arr[j + 1]:
            #     arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # ---------------------------------------------

        # Ee pass lo oka swap kuda jaragakapothe
        # Array already sorted ani artham
        if not swapped:
            break  # Early stop (optimization)

    return arr  # Sorted array return chestam


