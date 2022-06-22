import pathlib
import numpy as np

ROOT_PATH = pathlib.Path(__file__).parent.parent
DATA_DIR = ROOT_PATH / "data"
OUTPUT_DIR = ROOT_PATH / "output"
OUTPUT_FILE = OUTPUT_DIR / "game_data.xlsx"
INCOMING_OUTPUT_FILE = OUTPUT_DIR / "Thesis analysis v3.xlsx"
EARLY_ACCESS = DATA_DIR / "early_access.xlsx"
EX_EARLY_ACCESS = DATA_DIR / "ex_early_access.xlsx"
INDIE_FILE = DATA_DIR / "indie.xlsx"
DATA_FILES = list(DATA_DIR.glob(r"*.xlsx"))
DATA_SHEET = "Sheet1"
SCORE_COLUMN = "Score rank(Userscore / Metascore)"
SCORE_COLUMN_CLEAN = "Score (%)"
GAME_COLUMN = "Game"
RELEASE_COLUMN = "Release date"
RELEASE_FORMAT = "%b %d, %Y"
PRICE_COLUMN = "Price"
PRICE_BINS = [0, 10, 30, 50, np.inf]
PRICE_LABELS = [1, 2, 3, 4]
PRICE_CATEGORY_COLUMN = "Price Category"
OWNER_COLUMN = "Owners"
OWNER_LOWER_COLUMN = "Owners lower bound"
OWNER_UPPER_COLUMN = "Owners upper bound"
PLAYTIME_COLUMN = "Playtime (Median)"
DEVELOPER_COLUMN = "Developer(s)"
MULTI_DEVELOPER_COLUMN = "Multi Dev"
PUBLISHER_COLUMN = "Publisher(s)"
EARLY_ACCESS_COLUMN = "Early access"
INDIE_COLUMN = "Indie"
GAME_ID_COLUMN = "gameid"
GAME_COLUMN_RENAME = {GAME_ID_COLUMN: GAME_COLUMN}
INCOMING_OUTPUT_FILE_COLUMNS = [
    GAME_COLUMN,
    "earlyaccessnum",
    "circulation",
    "circulationCOPY",
    "ownergroups",
]
EXPORT_COLUMNS = [
    GAME_COLUMN,
    RELEASE_COLUMN,
    PRICE_COLUMN,
    PRICE_CATEGORY_COLUMN,
    SCORE_COLUMN_CLEAN,
    OWNER_LOWER_COLUMN,
    OWNER_UPPER_COLUMN,
    PLAYTIME_COLUMN,
    DEVELOPER_COLUMN,
    MULTI_DEVELOPER_COLUMN,
    PUBLISHER_COLUMN,
    EARLY_ACCESS_COLUMN,
    INDIE_COLUMN,
]
