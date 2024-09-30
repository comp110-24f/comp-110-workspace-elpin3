"""CQ04 - Coordinates"""

__author__ = "730768189"


def get_coords(sx: str, ys: str) -> None:
    """Prints out input strings in coord form"""
    xindex: int = 0
    yindex: int = 0
    while xindex < len(sx):
        while yindex < len(ys):
            print("(" + sx[xindex] + "," + ys[yindex] + ")")
            yindex += 1
        yindex = 0
        xindex += 1
