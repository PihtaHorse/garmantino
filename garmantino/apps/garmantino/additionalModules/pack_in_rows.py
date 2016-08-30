from itertools import cycle


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
    def pack_in_rows_by_position(cells_in_rows, positions, *properties):
        row_len = cycle(cells_in_rows)
        positions = list(sorted(positions))
        cells = PackInRows.make_cells(len(positions), properties)

        rows, cell_counter = [], 0

        while positions:
            row, cell_counter = PackInRows.make_row_by_position(next(row_len), cells, positions, cell_counter)
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
        row_len = cycle(cells_in_rows)
        print(min([len(values) for name, values in properties]))
        cells = PackInRows.make_cells(min([len(values) for name, values in properties]), properties)

        rows = []

        while cells:
            row = PackInRows.make_row_by_order(next(row_len), cells)
            rows.append(row)

        return rows

if __name__ == '__main__':
    cells_in_rows = [2, 3]
    positions = [1, 5, 8, 2, 4, 3]
    property_one = ['one', [11, 12, 13, 14, 15, 16]]
    property_two = ['two', [21, 22, 23, 24, 25, 26]]

    rows_positions = PackInRows.pack_in_rows_by_position(cells_in_rows, positions, property_one, property_two)
    rows_order = PackInRows.pack_in_rows_by_order(cells_in_rows, property_one, property_two)

    print('Positions:\n')
    [print(row) for row in rows_positions]
    print('Order:\n')
    [print(row) for row in rows_order]
