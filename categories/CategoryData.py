from CategoryEnum import CategoryEnum
import csv


def get_category_things(category_enum: CategoryEnum):
    category_name = category_enum.value

    csv_path = 'Data/{}.csv'.format(category_name)

    list_of_things = _get_list_of_things_from_csv(csv_path)
    return list_of_things


def _get_list_of_things_from_csv(csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)

        # transforms the reader into a list of stings, the first column of the CSV
        list_of_things = [row[0] for row in reader]

    return list_of_things
