from pathlib import Path

import pandas as pd
from lib.classes.AbstractDataSource import AbstractDataSource


class FileSource(AbstractDataSource):
    def __init__(self, folder_name: str, extension: str) -> None:
        self.folder_name = folder_name
        self.extension = extension
        self.input_path: Path = self.get_or_create_input_path()
        self.processed_files = set()
        self.dataframe_queue = []
        self.new_dataframe = pd.DataFrame()
        self.full_dataframe = pd.DataFrame()

    def get_or_create_input_path(self) -> Path:
        input_path = Path('..') / 'data' / self.folder_name

        if not input_path.exists():
            input_path.mkdir(parents=True)

        return input_path

    def check_for_new_files(self) -> list[Path]:
        return [
            file_path
            for file_path in self.input_path.iterdir()
            if file_path not in self.processed_files
            and file_path.suffix == self.extension
        ]

    def get_data(self, file_paths: list[Path]) -> None:
        pass

    def update_full_dataframe(self) -> None:
        self.new_dataframe = pd.concat(self.dataframe_queue, ignore_index=True)
        self.dataframe_queue.clear()

        self.full_dataframe = pd.concat(
            [self.full_dataframe, self.new_dataframe],
            ignore_index=True,
        )

    def save_data(self, filename: str = 'consolidated.csv') -> None:
        file_path = Path('..') / 'data' / filename

        if not file_path.exists():
            self.new_dataframe.to_csv(file_path, index=False)
        else:
            self.new_dataframe.to_csv(
                file_path, mode='a', sep=',', index=False, header=False,
            )

        self.new_dataframe = pd.DataFrame()

    def update_data(self):
        new_files = self.check_for_new_files()

        if new_files:
            print('New files detected:')
            print(new_files)
            self.get_data(new_files)
            self.update_full_dataframe()
            self.save_data()
            print('New data saved successfully.')
        else:
            print('There are no new files.')

    def show_processed_files(self):
        print(self.processed_files)
