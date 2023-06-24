import json
import csv
import pickle
import os


class Writer:
    def __init__(self, in_dct: dict, path: str, file_name: str):
        self.in_dct = in_dct
        self.path = path
        self.file_name = file_name

    def write_to_json(self):
        file_path = os.path.join(self.path, self.file_name + '.json')
        with open(file_path, 'w', encoding='utf-8') as f_out:
            json.dump(self.in_dct, f_out, indent=4)

    def write_to_csv(self):
        file_path = os.path.join(self.path, self.file_name + '.csv')
        data = [['path', 'type', 'name', 'size', ' parent dir', ]]
        for i_key, i_val in self.in_dct.items():
            data.append([i_key, *i_val.values()])
        with open(file_path, 'w', encoding='utf-8') as f_out:
            write_csv = csv.writer(f_out, dialect='excel', delimiter=';')
            write_csv.writerows(data)

    def write_to_pickle(self) -> None:
        file_path = os.path.join(self.path, self.file_name + '.pickle')
        with open(file_path, 'wb') as f_out:
            pickle.dump(self.in_dct, f_out)


class Formatter:
    def __init__(self, aim_path: str, total_dct: dict = None):
        self._aim_path = aim_path
        self._total_dct = self._walk_to_dir(total_dct)

    def _walk_to_dir(self, total_dct) -> dict[str, dict[str]]:
        if total_dct is None:
            total_dct = {}
            basic_path = os.path.split(os.path.abspath(self._aim_path))
            self._format_dict(total_dct,
                              os.path.join(*basic_path[:-1]),
                              basic_path[-1],
                              'D')

        for item in os.listdir(self._aim_path):
            check_path = os.path.join(self._aim_path, item)
            if os.path.isfile(check_path):
                self._format_dict(total_dct, self._aim_path, item, 'F')
            elif os.path.isdir(check_path):
                self._format_dict(total_dct, self._aim_path, item, 'D')
                self._aim_path = os.path.join(self._aim_path, item)
                self._walk_to_dir(total_dct)
        return total_dct

    def _format_dict(self, total_dct: dict[str, dict[str]],
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
                                   unit_size=self._count_size(os.path.join(path, item_name)),
                                   parent_dir=os.path.split(os.path.abspath(path))[-1])

    def get_total_dict(self):
        return self._total_dct

    def _count_size(self, count_path: str,
                    dir_size: int = 0) -> float:
        for dirpath, dirnames, filenames in os.walk(count_path):
            if filenames:
                dir_size += sum([os.path.getsize(os.path.join(dirpath, file))
                                 for file in filenames])
            if dirnames:
                dir_size += sum([self._count_size(os.path.join(dirpath, subdir))
                                 for subdir in dirnames])
        return dir_size


def main():
    tst_path = '/Users/jshuckbot/projects/python/top_level/part_1'
    result = Formatter(tst_path)
    Writer(result.get_total_dict(), os.getcwd(), 'path').write_to_json()
    Writer(result.get_total_dict(), os.getcwd(), 'path').write_to_pickle()
    Writer(result.get_total_dict(), os.getcwd(), 'path').write_to_csv()


if __name__ == '__main__':
    main()
