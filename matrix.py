import streamlit as st
import pandas as pd
from fractions import Fraction
#1 matrix calc from a 2d matrix

arr = [[0, 3, 1, 1], [1, -1, 0, 1], [2, 4, -2, 1]]

def rowAdd(arr1, scalar, arr2):
    newArr = []
    for i in range(len(arr1)):
        newArr.append(arr1[i] + scalar * arr2[i])
    return newArr

def rowScale(arr1, scalar):
    for i in range(len(arr1)):
        arr1[i] *= scalar
    return arr1

def printArr(array):
    for a in array:
        print(a)
    print(" ")


def rowReduce(arr):
    rows = len(arr)
    cols = len(arr[0])
    pivots = 0

    for i in range(cols):
        if (pivots < rows and pivots < cols):
            for j in range(rows):
                isPivot = True
                for x in range(i):
                    if arr[j][x] != 0:
                        isPivot = False
                if isPivot and arr[j][i] != 0:
                    #print(f"setting {j} to {1/arr[j][i]} times what it is")
                    arr[j] = rowScale(arr[j], 1/arr[j][i])
                    for tempI in range(rows):
                        if tempI != j:
                            scalar = -arr[tempI][i] # negative times what the pivot position is
                            arr[tempI] = rowAdd(arr[tempI], scalar, arr[j])
                            #print(f"setting {tempI} to it plus {scalar} plus row {j}")
                    pivots += 1
                    arr[j], arr[pivots-1] = arr[pivots-1], arr[j]
                    break
        else:
            break
    return arr



#2 format page that can build a matrix, take input from streamlit

def input_fields():
    st.sidebar.header("Select your number of rows and columns:")
    numRows = st.sidebar.number_input("Rows", min_value=1) # 1st new thing
    numCols = st.sidebar.number_input("Columns", min_value=1)
    st.subheader("Enter your matrix")
    dataframe = []
    for i in range(numRows):
        d = []
        for j in range(numCols):
            d.append(0)
        dataframe.append(d)
    edited_df = st.data_editor(dataframe, hide_index=True) # 2nd new thing

    if st.button("Reduce!"): # 3rd new thing
        reduced = rowReduce(edited_df)
        reducedDataFrame = st.data_editor(reduced, hide_index=True)

    st.write("---")
    st.write("---")
    st.write("Built by Thomas Becker :)")

input_fields()
