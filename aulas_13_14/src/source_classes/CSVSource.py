from pathlib import Path

import pandas as pd
from source_classes.FileSource import FileSource


class CSVSource(FileSource):
    def __init__(
            self,
            folder_name: str = 'csv_files',
            extension: str = '.csv',
        ) -> None:
        super().__init__(folder_name, extension)

    def get_data(self, file_paths: list[Path]) -> None:
        for file in file_paths:
            try:
                self.dataframe_queue.append(pd.read_csv(file))
                self.processed_files.add(file)
            except Exception as e:
                print(f'An error occurred while trying to read {file}.')
                print(e)
                continue
