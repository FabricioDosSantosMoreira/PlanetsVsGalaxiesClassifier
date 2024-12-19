from pathlib import Path
import re

import sys
from typing import Callable, List, Optional, Tuple

from PyTabFy.Dummy import get_japanese_movies_data
from PyTabFy.PyTUtils import get_terminal_width
from PyTabFy.PyTConfigs import TableConfigs
from PyTabFy.PyTCore.Types import TableData
from PyTabFy.PyTCore.Tables import (
    CenterAlignedTable, 
    LeftAlignedTable,
    RightAlignedTable,
    DefaultTable,
)
from PyTabFy.PyTEnums import (
    StringLengthValidation,
    StringSlicingMode, 
    StringFunctions, 
    StringBreakMode,
    TableFitMode, 
    TableSymbols,
    Alignment,
)

def validate_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Divide o conteúdo por blocos com duas ou mais linhas em branco como separador
    blocks = re.split(r"\n{2,}", content)

    list_of_nasa_id = []
    list_of_credits = []
    list_of_links = []
    for block in blocks:
        block_content = block.split('\n')

        _ = block_content[0]
        list_of_nasa_id.append(block_content[1][8::].removesuffix(' '))
        list_of_credits.append(block_content[2][8::].removesuffix(' '))
        list_of_links.append(block_content[3][5::].removesuffix(' '))

    print(len(list_of_nasa_id))
    print(len(list_of_credits))
    print(len(list_of_links))

    return list_of_nasa_id, list_of_credits, list_of_links

def tabfy(
        ids,
        credits,
        links,
        file_path,
        title
    ) -> None:

    class CustomConfigs(TableConfigs):
        
        def __init__(self) -> None:
            super().__init__()

            self.table_fit_mode = TableFitMode.MAX_TABLE_FIT
            self.table_symbols  = TableSymbols.DEFAULT_CLI
            #self.min_table_size = get_terminal_width(multiplier=0.75)
            self.max_table_size = 190

            self.string_lenght_validation = StringLengthValidation.WCSWIDTH  
            self.string_slicing_mode      = StringSlicingMode.STRING_END
            self.string_break_mode        = StringBreakMode.BREAK_DYNAMIC

            self.string_delimiters        =  ['...', ]

            self.max_title_string_lenght    = sys.maxsize
            self.max_header_strings_lenght  = [sys.maxsize, ]
            self.max_content_strings_lenght = [20, 60, sys.maxsize]

            self.title_string_function    = StringFunctions.STR_TITLE
            self.header_strings_function  = [StringFunctions.STR_KEEP_AS_IS, ]
            self.content_strings_function = [StringFunctions.STR_KEEP_AS_IS, ]

            self.title_left_padding     = 2
            self.title_right_padding    = 1
            self.header_left_paddings   = [2, ]
            self.header_right_paddings  = [1, ]
            self.content_left_paddings  = [2, ]
            self.content_right_paddings = [1, ]

            self.upper_title_empty_border_size = 1
            self.lower_title_empty_border_size = 1
            self.upper_header_empty_border_size = 0
            self.lower_header_empty_border_size = 0
            self.upper_content_empty_border_size = 0 
            self.lower_content_empty_border_size = 0 

            self.force_alternating_chars_respect = False
            self.enable_multiline = True
            self.force_display = True
            self.margin = 0

    custom_configs = CustomConfigs()

    headers = ['NASA ID', 'Credits', 'Image Link']

    contents = []
    for i in range(len(ids)):
        contents.append([ids[i], credits[i], links[i]])

    data = TableData().set_data(title=title, headers=headers, contents=contents)

    table = DefaultTable(custom_configs=custom_configs)
    table.build(data).log_table(file_path=file_path, border_between_content=True)


# Exemplo de uso
# ids, credits, links = validate_file("Dataset/Credits for Galaxy Images.txt")
# tabfy(ids, credits, links, Path('C:/Users/fabri/Desktop/PlanetsVsGalaxies/galaxies.txt'), "Galaxies Images Credits")

ids, credits, links = validate_file("Dataset/Credits for Planets Images.txt")
tabfy(ids, credits, links, Path('C:/Users/fabri/Desktop/PlanetsVsGalaxies/planet.txt'), "Planets Images Credits")
