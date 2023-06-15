import json
import csv
import pickle
import os


def write_to_json(in_dct: dict, path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name + '.json')
    with open(file_path, 'w', encoding='utf-8') as f_out:
        json.dump(in_dct, f_out, indent=4)


def write_to_csv(in_dct: dict, path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name + '.csv')
    data = [['path', 'type', 'name', 'size', ' parent dir', ]]
    for i_key, i_val in in_dct.items():
        data.append([i_key, *i_val.values()])
    with open(file_path, 'w', encoding='utf-8') as f_out:
        write_csv = csv.writer(f_out, dialect='excel', delimiter=';')
        write_csv.writerows(data)


def write_to_pickle(in_dct: dict, path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name + '.pickle')
    with open(file_path, 'wb') as f_out:
        pickle.dump(in_dct, f_out)


def format_dict(total_dct: dict[str, dict[str]],
                path: str,
                item_name: str,
                item_type: str) -> None:
    if item_type == 'F':
        total_dct[path] = dict(unit_type='File',
                               unit_name=item_name,
                               unit_size=os.path.getsize(os.path.join(path, item_name)),
                               parent_dir=os.path.split(path)[-1])
    elif item_type == 'D':
        total_dct[path] = dict(unit_type='Directory',
                               unit_name=item_name,
                               unit_size=count_size(os.path.join(path, item_name)),
                               parent_dir=os.path.split(os.path.abspath(path))[-1])


def count_size(count_path: str,
               dir_size: int = 0) -> float:
    for dirpath, dirnames, filenames in os.walk(count_path):
        if filenames:
            dir_size += sum([os.path.getsize(os.path.join(dirpath, file))
                             for file in filenames])
        if dirnames:
            dir_size += sum([count_size(os.path.join(dirpath, subdir))
                             for subdir in dirnames])
    return dir_size


def walk_to_dir(aim_path: str,
                total_dct: dict = None) -> dict[str, dict[str]]:
    if total_dct is None:
        total_dct = {}
        basic_path = os.path.split(os.path.abspath(aim_path))
        format_dict(total_dct,
                    os.path.join(*basic_path[:-1]),
                    basic_path[-1],
                    'D')

    for item in os.listdir(aim_path):
        check_path = os.path.join(aim_path, item)
        if os.path.isfile(check_path):
            format_dict(total_dct, aim_path, item, 'F')
        elif os.path.isdir(check_path):
            format_dict(total_dct, aim_path, item, 'D')
            walk_to_dir(os.path.join(aim_path, item), total_dct)
    return total_dct


def main():
    tst_path = '/Users/jshuckbot/projects/python/top_level/part_1'
    result = walk_to_dir(tst_path)
    write_to_json(result, os.getcwd(), 'path')
    write_to_pickle(result, os.getcwd(), 'path')
    write_to_csv(result, os.getcwd(), 'path')


if __name__ == '__main__':
    main()
