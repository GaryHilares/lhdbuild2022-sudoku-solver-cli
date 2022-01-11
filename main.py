import queue
import sys
import json

sudoku_9_unsolved = [
    ["9", ".", ".", ".", ".", ".", "6", "4", "5"],
    [".", ".", "1", ".", "8", ".", ".", "9", "."],
    [".", ".", "5", "9", "4", ".", "7", ".", "."],
    [".", "2", "6", "4", ".", ".", ".", "5", "."],
    [".", ".", "3", "6", "1", "8", "4", ".", "9"],
    ["8", ".", ".", ".", ".", ".", ".", "7", "."],
    ["4", "5", "2", "8", "6", "1", ".", ".", "."],
    ["7", "1", ".", "3", ".", "4", ".", ".", "2"],
    [".", ".", ".", ".", "9", "7", "5", "1", "."]
]

def is_valid(sudoku):
    if len(sudoku) == 0:
        return True
    n = len(sudoku)
    for lst in sudoku:
        if len(lst) != n:
            return False
    for lst in sudoku:
        for el in lst:
            if el != '.' and lst.count(el) > 1:
                return False
    for i in range(n):
        lst = [lst[i] for lst in sudoku]
        for el in lst:
            if el != '.' and lst.count(el) > 1:
                return False
    return True


def solve(sudoku):
    to_update = queue.Queue()
    if not is_valid(sudoku):
        return sudoku
    n = len(sudoku)
    for index_x, lst in enumerate(sudoku):
        for index_y, el in enumerate(lst):
            if el == '.':
                sudoku[index_x][index_y] = list(
                    [str(i) for i in range(1, n + 1)])
                to_update.put((index_x, index_y))

    def get_vertical_elements(matrix, index_x):
        for i in matrix[index_x]:
            yield i

    def get_horizontal_elements(matrix, index_y):
        for i in [lst[index_y] for lst in matrix]:
            yield i

    def get_elements_in_region(matrix_9x9, index_x, index_y):
        region_index_x = index_x // 3
        region_index_y = index_y // 3
        corner_index_x = region_index_x * 3
        corner_index_y = region_index_y * 3
        for y_offset in range(3):
            for x_offset in range(3):
                yield matrix_9x9[corner_index_x + x_offset][corner_index_y + y_offset]
        
    def is_list_with_one_element(x) -> bool:
        return type(x) == list and len(x) == 1

    def element_in_sudoku_vertical_list(el, index_x) -> bool:
        return el in get_vertical_elements(sudoku, index_x)

    def element_in_sudoku_horizontal_list(el, index_y) -> bool:
        return el in get_horizontal_elements(sudoku, index_y)

    def element_in_9x9_sudoku_region(el, index_x, index_y) -> bool:
        return el in get_elements_in_region(sudoku, index_x, index_y)
    
    def only_one_element_in_vertical_list_with_number(stringified_number, index_x) -> bool:
        return sum([1 for el in get_vertical_elements(sudoku, index_x) if stringified_number in el]) == 1
    
    def only_one_element_in_horizontal_list_with_number(stringified_number, index_y) -> bool:
        return sum([1 for el in get_horizontal_elements(sudoku, index_y) if stringified_number in el]) == 1
    
    def only_one_element_in_region_with_number(stringified_number, index_x, index_y) -> bool:
        return sum([1 for el in get_elements_in_region(sudoku, index_x, index_y) if stringified_number in el]) == 1
    
    while not to_update.empty():
        index_x, index_y = to_update.get()
        if type(sudoku[index_x][index_y]) != list:
            continue
        new_value = sudoku[index_x][index_y].copy()
        for stringified_number in sudoku[index_x][index_y]:
            if element_in_sudoku_horizontal_list(stringified_number, index_y) \
                    or element_in_sudoku_vertical_list(stringified_number, index_x) \
                    or element_in_9x9_sudoku_region(stringified_number, index_x, index_y):
                new_value.remove(stringified_number)
            only_one_possible = only_one_element_in_vertical_list_with_number(stringified_number, index_x) \
                or only_one_element_in_horizontal_list_with_number(stringified_number, index_y) \
                or only_one_element_in_region_with_number(stringified_number, index_x, index_y)
            if is_list_with_one_element(sudoku[index_x][index_y]) \
                    or only_one_possible:
                new_value = stringified_number if only_one_possible else sudoku[index_x][index_y][0]
                for index, element in enumerate(get_vertical_elements(sudoku, index_x)):
                    if type(element) == list and index != index_y:
                        to_update.put((index_x, index))
                for index, element in enumerate(get_horizontal_elements(sudoku, index_y)):
                    if type(element) == list and index != index_x:
                        to_update.put((index, index_y))
                for index, element in enumerate(get_elements_in_region(sudoku, index_x, index_y)):
                    if type(element) == list and (index % 3 != index_x % 3 and index % 3 != index_y % 3):
                        to_update.put((index_x // 3 * 3 + index %
                                      3, index_y // 3 * 3 + index // 3))
                break
        sudoku[index_x][index_y] = new_value
    return sudoku


def main():
    if len(sys.argv) < 2:
        print("Please pass the sudoku path as argument.")
    sudoku_path = sys.argv[1]
    sudoku = []
    with open(sudoku_path) as ifile:
        sudoku = json.load(ifile)
    solution = solve(sudoku)
    for lst in solution:
        print(lst)

if __name__ == '__main__':
    main()
