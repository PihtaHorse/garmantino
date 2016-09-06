from itertools import cycle, chain


class PackInRows:
    @staticmethod
    def create_empty_row(row_len):
        return [None for i in range(row_len)]

    @staticmethod
    def make_cells(cells_number, properties):
        return [{name: values[i] for name, values in properties} for i in range(cells_number)]

    @staticmethod
    def make_row_by_position(row_len, cells, positions, cell_counter):
        row = []
        for i in range(row_len):
            if positions and cell_counter == positions[0]:
                cell = cells.pop(0)
                positions.pop(0)
            else:
                cell = None

            cell_counter += 1
            row.append(cell)

        return row, cell_counter

    @staticmethod
    def pack_in_rows_by_position(cells_in_rows, positions, *properties, firsts_rows_lens=[]):
        row_len_iterator = iter(cells_in_rows)
        firsts_rows_lens_iterator = iter(firsts_rows_lens)
        positions = list(sorted(positions))
        cells = PackInRows.make_cells(len(positions), properties)

        rows, cell_counter = [], 0

        while positions:
            row, cell_counter = PackInRows.make_row_by_position(next(row_len_iterator), cells, positions, cell_counter)
            rows.append(row)

        return rows

    @staticmethod
    def make_row_by_order(row_len, cells):
        row = []
        for i in range(row_len):
            if cells:
                row.append(cells.pop(0))
            else:
                row.append(None)

        return row

    @staticmethod
    def pack_in_rows_by_order(cells_in_rows, *properties):
        row_len = iter(cells_in_rows)
        cells = PackInRows.make_cells(min([len(values) for name, values in properties]), properties)

        rows = []

        while cells:
            row = PackInRows.make_row_by_order(next(row_len), cells)
            rows.append(row)

        return rows

if __name__ == '__main__':
    property_one = ['one', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
    property_two = ['two', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']]

    cells_in_rows = chain([5], cycle([2, 3]))
    positions = [1, 5, 8, 2, 4, 3]
    rows_positions = PackInRows.pack_in_rows_by_position(cells_in_rows, positions, property_one, property_two)

    cells_in_rows = chain([5], cycle([2, 3]))
    rows_order = PackInRows.pack_in_rows_by_order(cells_in_rows, property_one, property_two)

    print('Positions:\n')
    [print(row) for row in rows_positions]
    print('Order:\n')
    [print(row) for row in rows_order]
