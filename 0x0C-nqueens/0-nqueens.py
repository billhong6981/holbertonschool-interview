#!/usr/bin/python3
"""Solves NQueens problem using Backtracking Algorithm
"""
import sys
import copy
LIFOCache = __import__('lifo_cache').LIFOCache
board_cache = LIFOCache()


def save_result(board, n):
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                a = [i, j]
                solution.append(a)
    board_cache.result.append(solution)
    print(solution)

def save_to_cache(board, n, col):
    """save each prosible solution to cache
    """
    for i in range(n):
        if isSafe(board, n, i, col):
            board[i][col] = 1
            if col == n-1:
                save_result(board, n)
                return
            else:
                key = str(i) + "x" + str(col)
                x = copy.deepcopy(board)
                board_cache.put(key, x)
                board[i][col] = 0

def pop_from_cache(n):
    dic = board_cache.pop_lifo()
    a_key = [x for x in dic.keys()]
    key = a_key[0]
    row = int(key[0])
    col = int(key[-1])
    board = dic[key]
    save_to_cache(board, n, col+1)

def isSafe(board, n, row, col):
    """A function to check if a queen can be place on board[row][col]
    """
    # check the row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    #check lower diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    #check upper diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQueens(board, n, col):
    """backtracking recursively to solve NQueens problem
    """
    #recursion function exit point
    if col >= n:
        return True

    #consider this column and try place Queen in all rows one by one
    for i in range(n):
        if isSafe(board, i, col):
            #place this queen in board[i][col]
            board[i][col] = 1
            if solveNQueens(board, n, col + 1) == True:
                return True

            #if not a solution, then reset to 0
            board[i][col] = 0

    #if the Queen can not be placed in any row in this column, then False
    return False

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for i in range(n)] for i in range(n)]

    save_to_cache(board, n, 0)

    #pop each possible frame to find out solution
    while len(board_cache.key_list) != 0:
        pop_from_cache(n)
