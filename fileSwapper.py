def swapfiledata():
    firstFile = input("Enter the first file name: \n")
    secondFile = input("Enter the second file name: \n")

    with open(firstFile, 'r') as file1:
        firstFileData = file1.read()

    with open(secondFile, 'r') as file2:
        secondFileData = file2.read()

    with open(firstFile, 'w+') as fileA:
        fileA.write(secondFileData)
    with open(secondFile, 'w+') as fileB:
        fileB.write(firstFileData)
    print("\nSwapped File Data Successfully! ")
    

swapfiledata()
