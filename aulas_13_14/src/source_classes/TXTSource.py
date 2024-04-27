from pathlib import Path

import pandas as pd
from source_classes.FileSource import FileSource


class TXTSource(FileSource):
    def __init__(
            self,
            folder_name: str = 'txt_files',
            extension: str = '.txt',
        ) -> None:
        super().__init__(folder_name, extension)

    def get_data(self, file_paths: list[Path]) -> None:
        for file in file_paths:
            try:
                # Assume the .txt files are tabulated
                self.dataframe_queue.append(pd.read_csv(file, sep='\t'))
                self.processed_files.add(file)
            except Exception as e:
                print(f'An error occurred while trying to read {file}.')
                print(e)
                continue
