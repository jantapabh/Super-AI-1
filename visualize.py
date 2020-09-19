# {
#   "nbformat": 4,
#   "nbformat_minor": 0,
#   "metadata": {
#     "colab": {
#       "name": "Homework#1_22p21s0202.ipynb",
#       "provenance": [],
#       "collapsed_sections": []
#     },
#     "kernelspec": {
#       "name": "python3",
#       "display_name": "Python 3"
#     }
#   },
#   "cells": [
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "kA-wEWQmBZSA",
#         "colab_type": "text"
#       },
#       "source": [
#         "0. เขียนโปรแกรมหาค่าสูงสุดในลิสต์"
#       ]
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "12Y9f70glxK2",
#         "colab_type": "code",
#         "colab": {
#           "base_uri": "https://localhost:8080/",
#           "height": 34
#         },
#         "outputId": "b15a88f9-9e96-4a4c-aefa-e2f8eb8c8069"
#       },
#       "source": [
#         "# Python3 program to find maximum in List\n",
#         "#Loop For find Max\n",
#         "def largest(arr,number): \n",
#         "  \n",
#         "    # Initialize maximum element \n",
#         "    maxValue = arr[0] \n",
#         "  \n",
#         "    for i in range(1, number): \n",
#         "        if arr[i] > maxValue: \n",
#         "            maxValue = arr[i] \n",
#         "    return maxValue\n",
#         "  \n",
#         "# Driver Code \n",
#         "arr = [10, 324, 45, 90, 9808, 888, 5, 5632, 1000,999997] \n",
#         "number = len(arr) \n",
#         "Ans = largest(arr,number) \n",
#         "print (\"Largest in given array is\",Ans) "
#       ],
#       "execution_count": null,
#       "outputs": [
#         {
#           "output_type": "stream",
#           "text": [
#             "Largest in given array is 999997\n"
#           ],
#           "name": "stdout"
#         }
#       ]
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "bK9H3UWrIePb",
#         "colab_type": "code",
#         "colab": {
#           "base_uri": "https://localhost:8080/",
#           "height": 34
#         },
#         "outputId": "ff3bee4f-ba9b-4846-8b21-cf59d32ef90b"
#       },
#       "source": [
#         "#Use Numpy Function\n",
#         "import numpy as np\n",
#         "\n",
#         "arr = np.array([11, 12, 13, 14, 15, 16, 17, 15, 11, 12, 14, 15, 16, 17])\n",
#         "maxElement = np.amax(arr)\n",
#         "print('Max element from Numpy Array : ', maxElement)"
#       ],
#       "execution_count": null,
#       "outputs": [
#         {
#           "output_type": "stream",
#           "text": [
#             "Max element from Numpy Array :  17\n"
#           ],
#           "name": "stdout"
#         }
#       ]
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "N6Q6xFohKGaT",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "#Input Number From Users\n",
#         "import numpy as np\n",
#         "\n",
#         "input_string = input(\"Enter a list elements : \")\n",
#         "print(\"\\n\")\n",
#         "userList = input_string.split()\n",
#         "print(\"user list is \", userList)\n",
#         " \n",
#         "# Find Max list elements use numpy\n",
#         "arr = np.array(userList)\n",
#         "largest_number = max(arr);\n",
#         "print(\"Max value is : \",largest_number)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "5rhhSHUNBcFw",
#         "colab_type": "text"
#       },
#       "source": [
#         "1. เขียน 8 puzzle ใช้ A* Algorithm\n",
#         "\n",
#         "```\n",
#         "# Run with VScode\n",
#         "```\n",
#         "\n"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "KdswtK6YVLp3",
#         "colab_type": "text"
#       },
#       "source": [
#         "***Start State : ***"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "6hZg6JggVINm",
#         "colab_type": "text"
#       },
#       "source": [
#         "![Start State.PNG](data:image/png;base64,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)"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "g2Y0wfovVRek",
#         "colab_type": "text"
#       },
#       "source": [
#         "**Goal State**"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "-a3QBoTwVPJK",
#         "colab_type": "text"
#       },
#       "source": [
#         "![GoalState.PNG](data:image/png;base64,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)"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "B2jogOveVeo0",
#         "colab_type": "text"
#       },
#       "source": [
#         "CODE :"
#       ]
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "-bb4U-tcSha7",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "from copy import deepcopy\n",
#         "from colorama import Fore, Back, Style\n",
#         "\n",
#         "DIRECTIONS = {\"U\": [-1, 0], #ขึ้น\n",
#         "              \"D\": [1, 0],  #ลง\n",
#         "              \"L\": [0, -1], #ซ้าย\n",
#         "              \"R\": [0, 1]}  #ขวา\n",
#         "\n",
#         "END = [[1, 2, 3],  #กำหนด state เริ่มต้น\n",
#         "       [4, 5, 6],\n",
#         "       [7, 8, 0]]\n",
#         "\n",
#         "# unicode\n",
#         "left_down_angle = '\\u2514'  #กำหนดทิศทางลงด้านซ้าย\n",
#         "right_down_angle = '\\u2518' #กำหนดทิศทางลงด้านขวา\n",
#         "right_up_angle = '\\u2510'   #กำหนดทิศทางขึ้นด้านขวา\n",
#         "left_up_angle = '\\u250C'    #กำหนดทิศทางขึ้นด้านซ้าย\n",
#         "\n",
#         "middle_junction = '\\u253C'  #กำหนดโหนดส่วนกลาง\n",
#         "top_junction = '\\u252C'     #กำหนดโหนดส่วนบน\n",
#         "bottom_junction = '\\u2534'  #กำหนดโหนดส่วนล่าง\n",
#         "right_junction = '\\u2524'   #กำหนดโหนดส่วนขวา\n",
#         "left_junction = '\\u251C'    #กำหนดโหนดส่วนซ้าย\n",
#         "\n",
#         "bar = Style.BRIGHT + Fore.CYAN + '\\u2502' + Fore.RESET + Style.RESET_ALL\n",
#         "dash = '\\u2500'\n",
#         "\n",
#         "first_line = Style.BRIGHT + Fore.CYAN + left_up_angle + dash + dash + dash + top_junction + dash + dash + dash + top_junction + dash + dash + dash + right_up_angle + Fore.RESET + Style.RESET_ALL\n",
#         "middle_line = Style.BRIGHT + Fore.CYAN + left_junction + dash + dash + dash + middle_junction + dash + dash + dash + middle_junction + dash + dash + dash + right_junction + Fore.RESET + Style.RESET_ALL\n",
#         "last_line = Style.BRIGHT + Fore.CYAN + left_down_angle + dash + dash + dash + bottom_junction + dash + dash + dash + bottom_junction + dash + dash + dash + right_down_angle + Fore.RESET + Style.RESET_ALL\n",
#         "\n",
#         "\n",
#         "def print_puzzle(array):\n",
#         "    print(first_line)\n",
#         "    for a in range(len(array)):\n",
#         "        for i in array[a]:\n",
#         "            if i == 0:\n",
#         "                print(bar, Back.RED + ' ' + Back.RESET, end=' ')\n",
#         "            else:\n",
#         "                print(bar, i, end=' ')\n",
#         "        print(bar)\n",
#         "        if a == 2:\n",
#         "            print(last_line)\n",
#         "        else:\n",
#         "            print(middle_line)\n",
#         "\n",
#         "\n",
#         "class Node:\n",
#         "    def __init__(self, current_node, previous_node, g, h, dir):\n",
#         "        self.current_node = current_node\n",
#         "        self.previous_node = previous_node\n",
#         "        self.g = g\n",
#         "        self.h = h\n",
#         "        self.dir = dir\n",
#         "\n",
#         "    def f(self):\n",
#         "        return self.g + self.h\n",
#         "\n",
#         "\n",
#         "def get_pos(current_state, element):\n",
#         "    for row in range(len(current_state)):\n",
#         "        if element in current_state[row]:\n",
#         "            return (row, current_state[row].index(element))\n",
#         "\n",
#         "\n",
#         "def euclidianCost(current_state):\n",
#         "    cost = 0\n",
#         "    for row in range(len(current_state)):\n",
#         "        for col in range(len(current_state[0])):\n",
#         "            pos = get_pos(END, current_state[row][col])\n",
#         "            cost += abs(row - pos[0]) + abs(col - pos[1])\n",
#         "    return cost\n",
#         "\n",
#         "\n",
#         "def getAdjNode(node):\n",
#         "    listNode = []\n",
#         "    emptyPos = get_pos(node.current_node, 0)\n",
#         "\n",
#         "    for dir in DIRECTIONS.keys():\n",
#         "        newPos = (emptyPos[0] + DIRECTIONS[dir][0], emptyPos[1] + DIRECTIONS[dir][1])\n",
#         "        if 0 <= newPos[0] < len(node.current_node) and 0 <= newPos[1] < len(node.current_node[0]):\n",
#         "            newState = deepcopy(node.current_node)\n",
#         "            newState[emptyPos[0]][emptyPos[1]] = node.current_node[newPos[0]][newPos[1]]\n",
#         "            newState[newPos[0]][newPos[1]] = 0\n",
#         "            # listNode += [Node(newState, node.current_node, node.g + 1, euclidianCost(newState), dir)]\n",
#         "            listNode.append(Node(newState, node.current_node, node.g + 1, euclidianCost(newState), dir))\n",
#         "\n",
#         "    return listNode\n",
#         "\n",
#         "\n",
#         "def getBestNode(openSet):\n",
#         "    firstIter = True\n",
#         "\n",
#         "    for node in openSet.values():\n",
#         "        if firstIter or node.f() < bestF:\n",
#         "            firstIter = False\n",
#         "            bestNode = node\n",
#         "            bestF = bestNode.f()\n",
#         "    return bestNode\n",
#         "\n",
#         "\n",
#         "def buildPath(closedSet):\n",
#         "    node = closedSet[str(END)]\n",
#         "    branch = list()\n",
#         "\n",
#         "    while node.dir:\n",
#         "        branch.append({\n",
#         "            'dir': node.dir,\n",
#         "            'node': node.current_node\n",
#         "        })\n",
#         "        node = closedSet[str(node.previous_node)]\n",
#         "    branch.append({\n",
#         "        'dir': '',\n",
#         "        'node': node.current_node\n",
#         "    })\n",
#         "    branch.reverse()\n",
#         "\n",
#         "    return branch\n",
#         "\n",
#         "\n",
#         "def main(puzzle):\n",
#         "    open_set = {str(puzzle): Node(puzzle, puzzle, 0, euclidianCost(puzzle), \"\")}\n",
#         "    closed_set = {}\n",
#         "\n",
#         "    while True:\n",
#         "        test_node = getBestNode(open_set)\n",
#         "        closed_set[str(test_node.current_node)] = test_node\n",
#         "\n",
#         "        if test_node.current_node == END:\n",
#         "            return buildPath(closed_set)\n",
#         "\n",
#         "        adj_node = getAdjNode(test_node)\n",
#         "        for node in adj_node:\n",
#         "            if str(node.current_node) in closed_set.keys() or str(node.current_node) in open_set.keys() and open_set[\n",
#         "                str(node.current_node)].f() < node.f():\n",
#         "                continue\n",
#         "            open_set[str(node.current_node)] = node\n",
#         "\n",
#         "        del open_set[str(test_node.current_node)]\n",
#         "\n",
#         "\n",
#         "if __name__ == '__main__':\n",
#         "    br = main([[6, 2, 8],\n",
#         "               [4, 7, 1],\n",
#         "               [0, 3, 5]])\n",
#         "\n",
#         "    print('total steps : ', len(br) - 1)\n",
#         "    print()\n",
#         "    print(dash + dash + right_junction, \"INPUT\", left_junction + dash + dash)\n",
#         "    for b in br:\n",
#         "        if b['dir'] != '':\n",
#         "            letter = ''\n",
#         "            if b['dir'] == 'U':\n",
#         "                letter = 'UP'\n",
#         "            elif b['dir'] == 'R':\n",
#         "                letter = \"RIGHT\"\n",
#         "            elif b['dir'] == 'L':\n",
#         "                letter = 'LEFT'\n",
#         "            elif b['dir'] == 'D':\n",
#         "                letter = 'DOWN'\n",
#         "            print(dash + dash + right_junction, letter, left_junction + dash + dash)\n",
#         "        print_puzzle(b['node'])\n",
#         "        print()\n",
#         "\n",
#         "    print(dash + dash + right_junction, 'ABOVE IS THE OUTPUT', left_junction + dash + dash)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "oK-WZdFtSnfc",
#         "colab_type": "text"
#       },
#       "source": [
#         "Start State -> ([[6, 2, 8],            \n",
#         "                 [4, 7, 1],\n",
#         "                 [0, 3, 5]])     "
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "qnG0gEbIS2He",
#         "colab_type": "text"
#       },
#       "source": [
#         "Goal State = [[1, 2, 3],\n",
#         "              [4, 5, 6],\n",
#         "              [7, 8, 0]]"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "WEnmj-EnUk9B",
#         "colab_type": "text"
#       },
#       "source": [
#         "**ผลการรันโปรแกรม :**"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "zAf7WHzaUqBW",
#         "colab_type": "text"
#       },
#       "source": [
#         "![1.PNG](data:image/png;base64,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)"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "zAmqF4BjVhlL",
#         "colab_type": "text"
#       },
#       "source": [
#         "![2.PNG](data:image/png;base64,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)"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "4OjDjNNHVi1b",
#         "colab_type": "text"
#       },
#       "source": [
#         "![3.PNG](data:image/png;base64,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)"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "xIJcoOtWVj6R",
#         "colab_type": "text"
#       },
#       "source": [
#         "![4.PNG](data:image/png;base64,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)"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "aC970mu2VlRI",
#         "colab_type": "text"
#       },
#       "source": [
#         "![5.PNG](data:image/png;base64,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)"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "MVFriGOpVmkH",
#         "colab_type": "text"
#       },
#       "source": [
#         "![6.PNG](data:image/png;base64,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)"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "sM9W7euABhot",
#         "colab_type": "text"
#       },
#       "source": [
#         "2. เขียน depth-first search พร้อมอะนิเมชั่น"
#       ]
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "7_8tjayo9eAp",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "graph = {\"A\":[\"D\",\"C\",\"B\"],\"B\":[\"E\"],\"C\":[\"G\",\"F\"],\"D\":[\"H\"],\"E\":[\"I\"],\"F\":[\"J\"]}"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "IYZisw5pBmIr",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "def dfs_non_recursive(graph, source):\n",
#         "\n",
#         "       if source is None or source not in graph:\n",
#         "\n",
#         "           return \"Invalid input\"\n",
#         "\n",
#         "       path = []\n",
#         "\n",
#         "       stack = [source]\n",
#         "\n",
#         "       while(len(stack) != 0):\n",
#         "\n",
#         "           s = stack.pop()\n",
#         "\n",
#         "           if s not in path:\n",
#         "\n",
#         "               path.append(s)\n",
#         "\n",
#         "           if s not in graph:\n",
#         "\n",
#         "               #leaf node\n",
#         "               continue\n",
#         "\n",
#         "           for neighbor in graph[s]:\n",
#         "\n",
#         "               stack.append(neighbor)\n",
#         "\n",
#         "       return \" \".join(path)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "4ESBh-Af9WqS",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "DFS_path = dfs_non_recursive(graph, \"A\")\n",
#         "\n",
#         "print(DFS_path)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "ZeFNfMYk90mo",
#         "colab_type": "text"
#       },
#       "source": [
#         "![01_intro_01.gif](data:image/gif;base64,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fNBydPDSfNByWvPRYMzba/DRYMzb3vLWLQ7fE83R2A0rGm7X9z0FGm7X900lGm7X9z0FGm7X900lGm7X9z0FGm7X900lGm7X9z0FGm7X900lb93i8D3R/xyN3bDy0WDM22vw0WDM297y0nzQcnTw0nzQclrT1Nt91HTQ1Nt91Frz1H7Q1GDw1H7Q1Jny1XwQ1m48daJWdYUT1xg91rny1jX+1pni6Z+eB57+6aTD2BtM4fh75YBN4amC2dK26GWA2dK26Lxy6AGs4fG86EKv4dyh25DM22+g25DM2xSj3Og76AGs3gNM9Xiy7lCu4UOw7lCu4eth3snr4aM+vt9dPutOBRb+zlde4RqOHwg+dgo+vOo93hJPP+tO5diNb1ceu9hdMCjeth5+6ib+6a+OJzSOLTK+BzSOLTIOPElOB0dOZj1u5IdOMVue4aA+3RRu1FdOMWlO6/8t7XKe3t1rbkB1nul3Pl+UHrVWW0GJLueHbsKYbueLXjeRXulkiOlzpek2xOkZ7ukye+Vr4+los7Bl4OqMXusXe+svVOxhcOwklexvmO9wn+19s+1cHu15uO1/3+3HOu6N0O3HOu5rtO9m3O+odO/enu+YP/CX3fCaMPCX3fCxr/H4BKusCgoaj0+wyqrPf/LISPMJ77Eyj/KM6uGJP/SjVPSfMPSjVPTPz/RT/wpMP/X3DzFon6UTIfayQPZif//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f//3f/8193//93//93//93//93//93//93//93//93//93//93//93//93//93//93//93//988jQQAAIfkEBTIAFgAs1QArAEoASgAABf+gJY5kaZ6WgYiDxVQVY7UWYqB4ru8o7P9AGG9IxBUQg6By6RsgCsXojkllSq+nqtaKjSIa2zCzsermbuK09WY2fdVwJbldituVdAtBce8DFQRmE36EPhNYBIOFixOBUXyLkQpSkZUVRQiWlmU6BmCakQ1sOqCWO5mlmzmfqaE5rZqvsJU4s7ElUK0OAAAJtFAjqKUBvL2qI0nDxcaVNCKpxMu+piLClQwHy7zTlZyaELvazLQj1w/ixdyRIgaWAtoH59ugKu7FDwsV8uPdFvYO3PapW+cPlkBQM2Yd1NRCYTqE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)"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "XVEDs_30BmZX",
#         "colab_type": "text"
#       },
#       "source": [
#         "3. เลือกข้อมูล 1 อย่างจาก Kaggle มาทำการ visualize ข้อมูลในรูปแบบกราฟต่างๆ"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "gXZ1VEBFXZ73",
#         "colab_type": "text"
#       },
#       "source": [
#         "เลือกข้อมูล Covid จากลิงค์ \n",
#         "[link text](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset?select=covid_19_data.csv)\n",
#         "\n",
#         " - Kaggle แสดงการ Visualize ข้อมูลโควิด\n",
#         "\n",
#         "Link Kaggle : https://www.kaggle.com/jantapabilheem/covid-visualize-22p21s0202-jan/edit"
#       ]
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "vMizQ-uwZlKQ",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "import pandas as pd\n",
#         "import datetime\n",
#         "import numpy as np\n",
#         "import math\n",
#         "\n",
#         "import matplotlib.pyplot as plt\n",
#         "import matplotlib.ticker as mtick\n",
#         "from numpy.polynomial.polynomial import polyfit\n",
#         "\n",
#         "#เลือกข้อมูลของโรคระบาด Covid-19 ซึ่งข้อมูลในแต่ละแถวนั้นก็จะรายงานจำนวนผู้ติดเชื้อสะสม จำนวนผู้เสียชีวิต และผู้ป่วยที่หายแล้วแบบอัพเดทในแต่ละวัน\n",
#         "\n",
#         "file_url=\"../input/novel-corona-virus-2019-dataset/covid_19_data.csv\"\n",
#         "df=pd.read_csv(file_url)\n",
#         "df.tail()\n",
#         "df=pd.read_csv(file_url)\n",
#         "# print(df)\n"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "NRZkiCCQhk5Q",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "countries_list=df['Country/Region'].unique()\n",
#         "\n",
#         "countries_list #List ประเทศที่ติดเชื้อโควิด"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "cP_2FFfqhm-Z",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "corona_study={}  #corona_study เพื่อเก็บจำนวนผู้ป่วย จำนวนผู้เสียชีวิต และจำนวนผู้ป่วยที่หายแล้วของแต่ละประเทศ ณ ปัจจุบัน \n",
#         "corona_average_daily_growth={}  #เพื่อเก็บจำนวนผู้ป่วยที่เพิ่มขึ้นเฉลี่ยต่อวันออกมาและจะทำการ for loop คำนวณข้อมูลของแต่ละประเทศ\n",
#         "\n",
#         "for country in countries_list:\n",
#         "    df_country=df[df['Country/Region']==country]\n",
#         "    \n",
#         "    df_country_by_date=df_country.groupby(['ObservationDate']).sum()\n",
#         "    corona_study[country]={}\n",
#         "    corona_study[country]['confirmed']=df_country_by_date['Confirmed'].max()\n",
#         "    corona_study[country]['death']=df_country_by_date['Deaths'].max()\n",
#         "    corona_study[country]['recovered']=df_country_by_date['Recovered'].max()\n",
#         "    confirmed_series=list(df_country_by_date['Confirmed'])\n",
#         "    corona_average_daily_growth[country]=np.mean(np.diff(confirmed_series))"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "RP5XS8_PhtDJ",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "corona_study['China'] = corona_study.pop('Mainland China')\n",
#         "corona_study['United States of America'] = corona_study.pop('US')\n",
#         "corona_study['United Kingdom'] = corona_study.pop('UK')\n",
#         "corona_study['Macedonia'] = corona_study.pop('North Macedonia')\n",
#         "corona_study['Azerbaijan'] = corona_study.pop(' Azerbaijan')\n",
#         "corona_study['Dominican Rep.'] = corona_study.pop('Dominican Republic')\n",
#         "corona_study['Czechia'] = corona_study.pop('Czech Republic')\n",
#         "corona_study['Bosnia and Herz.'] = corona_study.pop('Bosnia and Herzegovina')\n",
#         "corona_study['Guyana'] = corona_study.pop('French Guiana')\n",
#         "corona_study['eSwatini'] = corona_study.pop('Eswatini')\n",
#         "corona_study['Central African Rep.'] = corona_study.pop('Central African Republic')\n",
#         "corona_study['Eq. Guinea'] = corona_study.pop('Equatorial Guinea')\n",
#         "corona_study['Dem. Rep. Congo'] = corona_study.pop('Congo (Kinshasa)')\n",
#         "corona_study['Timor-Leste'] = corona_study.pop('East Timor')\n",
#         "corona_study['W. Sahara'] = corona_study.pop('Western Sahara')\n",
#         "corona_study['Myanmar'] = corona_study.pop('Burma')\n",
#         "corona_study['S. Sudan'] = corona_study.pop('South Sudan')\n",
#         "\n",
#         "corona_average_daily_growth['China'] = corona_average_daily_growth.pop('Mainland China')\n",
#         "corona_average_daily_growth['United States of America'] = corona_average_daily_growth.pop('US')\n",
#         "corona_average_daily_growth['United Kingdom'] = corona_average_daily_growth.pop('UK')\n",
#         "corona_average_daily_growth['Macedonia'] = corona_average_daily_growth.pop('North Macedonia')\n",
#         "corona_average_daily_growth['Azerbaijan'] = corona_average_daily_growth.pop(' Azerbaijan')\n",
#         "corona_average_daily_growth['Dominican Rep.'] = corona_average_daily_growth.pop('Dominican Republic')\n",
#         "corona_average_daily_growth['Czechia'] = corona_average_daily_growth.pop('Czech Republic')\n",
#         "corona_average_daily_growth['Bosnia and Herz.'] = corona_average_daily_growth.pop('Bosnia and Herzegovina')\n",
#         "corona_average_daily_growth['Guyana'] = corona_average_daily_growth.pop('French Guiana')\n",
#         "corona_average_daily_growth['eSwatini'] = corona_average_daily_growth.pop('Eswatini')\n",
#         "corona_average_daily_growth['Central African Rep.'] = corona_average_daily_growth.pop('Central African Republic')\n",
#         "corona_average_daily_growth['Eq. Guinea'] = corona_average_daily_growth.pop('Equatorial Guinea')\n",
#         "corona_average_daily_growth['Dem. Rep. Congo'] = corona_average_daily_growth.pop('Congo (Kinshasa)')\n",
#         "corona_average_daily_growth['Timor-Leste'] = corona_average_daily_growth.pop('East Timor')\n",
#         "corona_average_daily_growth['W. Sahara'] = corona_average_daily_growth.pop('Western Sahara')\n",
#         "corona_average_daily_growth['Myanmar'] = corona_average_daily_growth.pop('Burma')\n",
#         "corona_average_daily_growth['S. Sudan'] = corona_average_daily_growth.pop('South Sudan')"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "VF568hxahvVH",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "import collections\n",
#         "\n",
#         "counter = collections.Counter()\n",
#         "for d in [corona_study['Ireland'],corona_study['North Ireland']]: \n",
#         "    counter.update(d)\n",
#         "corona_study['Ireland']=dict(counter) \n",
#         "\n",
#         "counter = collections.Counter()\n",
#         "for d in [corona_study['Ireland'],corona_study['Republic of Ireland']]: \n",
#         "    counter.update(d)\n",
#         "corona_study['Ireland']=dict(counter) \n",
#         "\n",
#         "\n",
#         "counter = collections.Counter()\n",
#         "for d in [corona_study['Ireland'],corona_study['Republic of Ireland']]: \n",
#         "    counter.update(d)\n",
#         "corona_study['Ireland']=dict(counter) \n",
#         "\n",
#         "counter = collections.Counter()\n",
#         "for d in [corona_study['Dem. Rep. Congo'],corona_study['Congo (Brazzaville)']]: \n",
#         "    counter.update(d)\n",
#         "corona_study['Dem. Rep. Congo']=dict(counter) \n",
#         "\n",
#         "counter = collections.Counter()\n",
#         "for d in [corona_study['Dem. Rep. Congo'],corona_study['Republic of the Congo']]: \n",
#         "    counter.update(d)\n",
#         "corona_study['Dem. Rep. Congo']=dict(counter)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "5hNh0Rf-hxg3",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "import geopandas as  gpd\n",
#         "\n",
#         "world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))\n",
#         "world['confirmed'] = 0\n",
#         "world['death'] = 0\n",
#         "world['recovered'] = 0\n",
#         "world['active_case']=0\n",
#         "world['daily_growth']=0\n",
#         "world['death_rate']=0\n",
#         "world['recovered_rate']=0"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "7VT5nzy6hy4p",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "for country,row in corona_study.items():\n",
#         "    if (len(world.loc[world['name'] == country])>0):\n",
#         "        country_index=world.loc[world['name'] == country].index[0]\n",
#         "        world.at[country_index,'confirmed']=math.log(corona_study[country]['confirmed']+1)\n",
#         "        world.at[country_index,'death']=math.log(corona_study[country]['death']+1)\n",
#         "        world.at[country_index,'active_case']=math.log(corona_study[country]['confirmed']-corona_study[country]['death']-corona_study[country]['recovered']+1)\n",
#         "        world.at[country_index,'recovered']=math.log(corona_study[country]['recovered']+1)\n",
#         "        world.at[country_index,'death_rate']=math.log(100*(corona_study[country]['death']/corona_study[country]['confirmed'])+1)\n",
#         "        world.at[country_index,'recovered_rate']=math.log(100*(corona_study[country]['recovered']/corona_study[country]['confirmed'])+1)\n",
#         "        if (not math.isnan(corona_average_daily_growth[country])):\n",
#         "            world.at[country_index,'daily_growth']=math.log(corona_average_daily_growth[country]+1)\n",
#         "    else:\n",
#         "        print(country)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "08dauU4Zh1wX",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "fig, ax = plt.subplots(figsize  = (12, 8))\n",
#         "world.plot(column='confirmed', cmap='OrRd',ax=ax,figsize=(15, 10));\n",
#         "ax.set_title(\"Visualization of Confirmed case map\", fontsize=12)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "MsiwuvyTiAKR",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "fig, ax = plt.subplots(figsize  = (12, 8))\n",
#         "world.plot(column='active_case', cmap='OrRd',ax=ax,figsize=(15, 10));\n",
#         "ax.set_title(\"Visualization of Active case map\", fontsize=12)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "D-lfjcHPiCmJ",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "fig, ax = plt.subplots(figsize  = (12, 8))\n",
#         "world.plot(column='death', cmap='OrRd',ax=ax,figsize=(15, 10));\n",
#         "ax.set_title(\"Visualization of Death case map\", fontsize=12)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "GI5_TZn_iD5i",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "fig, ax = plt.subplots(figsize  = (12, 8))\n",
#         "world.plot(column='recovered', cmap='Greens',ax=ax,figsize=(15, 10));\n",
#         "ax.set_title(\"Visualization of Recovered case map\", fontsize=12)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "YSZGkRBFiFUB",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "fig, ax = plt.subplots(figsize  = (12, 8))\n",
#         "world.plot(column='death_rate', cmap='OrRd',ax=ax,figsize=(15, 10));\n",
#         "ax.set_title(\"Visualization of death rate map\", fontsize=12)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "db0j5TD4iG5u",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "fig, ax = plt.subplots(figsize  = (12, 8))\n",
#         "world.plot(column='recovered_rate', cmap='Greens',ax=ax,figsize=(15, 10));\n",
#         "ax.set_title(\"Visualization of recovered rate map\", fontsize=12)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "5iyBOuuUiIUU",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "fig, ax = plt.subplots(figsize  = (12, 8))\n",
#         "world.plot(column='daily_growth', cmap='OrRd',ax=ax,figsize=(15, 10));\n",
#         "ax.set_title(\"Visualization of daily growth of confirmed case map\", fontsize=12)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "boUGMa3si_pB",
#         "colab_type": "text"
#       },
#       "source": [
#         "**# Visualize ข้อมูลการ Shoping ขอผู้ใช้ Social media โดยนำมาวิเคราะห์เรื่องขอพฤติกรรมการใช้งานสื่ออินเตอร์เน็ตแลักสนซื้อสินค้า**"
#       ]
#     },
#     {
#       "cell_type": "markdown",
#       "metadata": {
#         "id": "zFvPJ2k0jH0-",
#         "colab_type": "text"
#       },
#       "source": [
#         "Link Data : (https://www.kaggle.com/rakeshrau/social-network-ads)\n",
#         "\n",
#         "Link Kaggle : https://www.kaggle.com22p21s0202-jan"
#       ]
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "c1apWBRombwn",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "# This Python 3 environment comes with many helpful analytics libraries installed\n",
#         "# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n",
#         "# For example, here's several helpful packages to load\n",
#         "\n",
#         "import numpy as np # linear algebra\n",
#         "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
#         "\n",
#         "# Input data files are available in the read-only \"../input/\" directory\n",
#         "# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
#         "\n",
#         "import os\n",
#         "for dirname, _, filenames in os.walk('/kaggle/input'):\n",
#         "    for filename in filenames:\n",
#         "        print(os.path.join(dirname, filename))\n",
#         "\n",
#         "# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n",
#         "# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "1Syp40lJw4q9",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "import datetime\n",
#         "import math\n",
#         "import matplotlib.pyplot as plt\n",
#         "import matplotlib.ticker as mtick\n",
#         "import seaborn as sns\n",
#         "from numpy.polynomial.polynomial import polyfit\n",
#         "\n",
#         "#เลือกข้อมูลของโรคระบาด Covid-19 ซึ่งข้อมูลในแต่ละแถวนั้นก็จะรายงานจำนวนผู้ติดเชื้อสะสม จำนวนผู้เสียชีวิต และผู้ป่วยที่หายแล้วแบบอัพเดทในแต่ละวัน\n",
#         "\n",
#         "file_url=\"../input/social-network-ads/Social_Network_Ads.csv\"\n",
#         "dataSet = pd.read_csv(file_url)\n",
#         "dataSet.head()\n",
#         "# dataSet.tail()\n",
#         "# print(df)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "0CF8Of-vw6nY",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "dataSet[\"Purchased\"].value_counts() #เลือกนับค่าในคอลัมล์ชื่อ Purchased โดยค่าที่ได้คือ 1 และ 0"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "Wo9v76Rkw8d5",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "dataSet.plot(kind=\"scatter\", x=\"EstimatedSalary\", y=\"Age\")"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "5GjMw_w4w93b",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "sns.jointplot(x=\"EstimatedSalary\", y=\"Age\", data=dataSet, size=5)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "9ZumwFW8w_3q",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "# One piece of information missing in the plots above is what species each plant is\n",
#         "# We'll use seaborn's FacetGrid to color the scatterplot by species\n",
#         "sns.FacetGrid(dataSet, hue=\"Purchased\", size=5) \\\n",
#         "   .map(plt.scatter, \"EstimatedSalary\", \"Age\") \\\n",
#         "   .add_legend()"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "jdpmtOJaxCR9",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "sns.boxplot(x=\"EstimatedSalary\", y=\"Age\", data=dataSet)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "89c1hfJwxD0l",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "ax = sns.boxplot(x=\"EstimatedSalary\", y=\"Age\", data=dataSet)\n",
#         "ax = sns.stripplot(x=\"EstimatedSalary\", y=\"Age\", data=dataSet, jitter=True, edgecolor=\"gray\")"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "3Dv9g_D0xEbu",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "sns.FacetGrid(dataSet, hue=\"Purchased\", size=6) \\\n",
#         "   .map(sns.kdeplot, \"Age\") \\\n",
#         "   .add_legend()"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "90KWYeEmxFrT",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "sns.pairplot(dataSet.drop(\"User ID\", axis=1), hue=\"Purchased\", size=3)"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "sFk01cDzxH1L",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         "dataSet.drop(\"EstimatedSalary\", axis=1).boxplot(by=\"Purchased\", figsize=(12, 6))"
#       ],
#       "execution_count": null,
#       "outputs": []
#     },
#     {
#       "cell_type": "code",
#       "metadata": {
#         "id": "ZI-OnWHVxIMR",
#         "colab_type": "code",
#         "colab": {}
#       },
#       "source": [
#         ""
#       ],
#       "execution_count": null,
#       "outputs": []
#     }
#   ]
# }