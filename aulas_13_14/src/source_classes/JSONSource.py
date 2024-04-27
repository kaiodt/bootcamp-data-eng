import json
from pathlib import Path

import pandas as pd
from source_classes.FileSource import FileSource


class JSONSource(FileSource):
    def __init__(
            self,
            folder_name: str = 'json_files',
            extension: str = '.json',
        ) -> None:
        super().__init__(folder_name, extension)

    def get_data(self, file_paths: list[Path]) -> None:
        for file in file_paths:
            try:
                with file.open('r', encoding='utf-8') as f:
                    self.dataframe_queue.append(pd.DataFrame(json.load(f)))

                self.processed_files.add(file)
            except Exception as e:
                print(f'An error occurred while trying to read {file}.')
                print(e)
                continue
