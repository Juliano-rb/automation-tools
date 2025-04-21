from enum import Enum


class Region(str, Enum):
    BR_PT = "br-pt"
    US_EN = "us-en"
    UK_EN = "uk-en"
    RU_RU = "ru-ru"
    WT_WT = "wt-wt"


class LicenseImage(str, Enum):
    ANY = "any"
    PUBLIC = "public"
    SHARE = "share"
    SHARE_COMMERCIALLY = "shareCommercially"
    MODIFY = "modify"
    MODIFY_COMMERCIALLY = "modifyCommercially"


class Size(str, Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    WALLPAPER = "Wallpaper"


class TypeImage(str, Enum):
    PHOTO = "photo"
    CLIPART = "clipart"
    GIF = "gif"
    TRANSPARENT = "transparent"
    LINE = "line"


class Color(str, Enum):
    COLOR = "color"
    MONOCHROME = "Monochrome"
    RED = "Red"
    ORANGE = "Orange"
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"
    PURPLE = "Purple"
    PINK = "Pink"
    BROWN = "Brown"
    BLACK = "Black"
    GRAY = "Gray"
    TEAL = "Teal"
    WHITE = "White"


class Layout(str, Enum):
    SQUARE = "Square"
    TALL = "Tall"
    WIDE = "Wide"
