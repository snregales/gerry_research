import pathlib

ROOT_PATH = pathlib.Path(__file__).parent.parent
DATA_DIR = ROOT_PATH / "data"
OUTPUT_DIR = ROOT_PATH / "output"
OUTPUT_FILE = OUTPUT_DIR / "game_data.xlsx"
EARLY_ACCESS = DATA_DIR / "early_access.xlsx"
EX_EARLY_ACCESS = DATA_DIR / "ex_early_access.xlsx"
DATA_FILES = list(DATA_DIR.glob(r"*.xlsx"))
DATA_SHEET = "Sheet1"
SCORE_COLUMN = "Score rank(Userscore / Metascore)"
SCORE_COLUMN_CLEAN = "Score (%)"
GAME_COLUMN = "Game"
RELEASE_COLUMN = "Release date"
PRICE_COLUMN = "Price"
OWNER_COLUMN = "Owners"
OWNER_LOWER_COLUMN = "Owners lower bound"
OWNER_UPPER_COLUMN = "Owners upper bound"
PLAYTIME_COLUMN = "Playtime (Median)"
DEVELOPER_COLUMN = "Developer(s)"
PUBLISHER_COLUMN = "Publisher(s)"
EARLY_ACCESS_COLUMN = "Early access"
EXPORT_COLUMNS = [
    GAME_COLUMN,
    RELEASE_COLUMN,
    PRICE_COLUMN,
    SCORE_COLUMN_CLEAN,
    OWNER_LOWER_COLUMN,
    OWNER_UPPER_COLUMN,
    PLAYTIME_COLUMN,
    DEVELOPER_COLUMN,
    PUBLISHER_COLUMN,
    EARLY_ACCESS_COLUMN,
]
