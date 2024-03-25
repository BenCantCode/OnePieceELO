import re
from mediawiki_dump.dumps import LocalFileDump
from mediawiki_dump.reader import DumpReaderArticles
import mediawiki_dump.tokenizer

dump = LocalFileDump('onepiece_pages_current.xml')
pages = DumpReaderArticles().read(dump)
chapters = sorted([page for page in pages if re.match('^Chapter \\d+$', page.title)], key=lambda page: int(page.title.split(" ")[1]))
summaries = {}

sagas = [
    {"name": "east_blue", "start": 1, "end": 100},
    {"name": "arabasta", "start": 101, "end": 217},
    {"name": "sky_island", "start": 218, "end": 302},
    {"name": "water_seven", "start": 303, "end": 441},
    {"name": "thriller_bark", "start": 442, "end": 489},
    {"name": "summit_war", "start": 490, "end": 597},
    {"name": "fish_man_island", "start": 598, "end": 653},
    {"name": "dressrosa", "start": 654, "end": 801},
    {"name": "whole_cake_island", "start": 802, "end": 908},
    {"name": "wano_country", "start": 909, "end": 1057},
    {"name": "final", "start": 1058, "end": 2000}
]

for chapter in chapters:
    number = int(chapter.title.split(" ")[1])
    summary = re.split("(?<!=)==[^=]", re.split("(?:== *Long Summary *==)", chapter.content)[1])[0].strip()
    summaries[number] = mediawiki_dump.tokenizer.clean(summary)

for saga in sagas:
    with open(f'summaries/{saga["name"]}_summary.txt', 'w') as file:
        for chapter in range(saga["start"], min(saga["end"], max(summaries.keys())) + 1):
            file.write(f"Chapter {chapter}\n\n{summaries[chapter]}\n\n")

