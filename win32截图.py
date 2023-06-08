import numpy as np
from win32con import SRCCOPY
from win32gui import GetDesktopWindow, GetWindowDC, DeleteObject, ReleaseDC
from win32ui import CreateDCFromHandle, CreateBitmap


def win(region):
    """
    region: tuple, (left, top, width, height)
                    左上x  左上y 宽度 高度
    """
    left, top, width, height = region
    hWin = GetDesktopWindow()
    hWinDC = GetWindowDC(hWin)
    srcDC = CreateDCFromHandle(hWinDC)
    memDC = srcDC.CreateCompatibleDC()
    bmp = CreateBitmap()
    bmp.CreateCompatibleBitmap(srcDC, width, height)
    memDC.SelectObject(bmp)
    memDC.BitBlt((0, 0), (width, height), srcDC, (left, top), SRCCOPY)
    array = bmp.GetBitmapBits(True)
    DeleteObject(bmp.GetHandle())
    memDC.DeleteDC()
    srcDC.DeleteDC()
    ReleaseDC(hWin, hWinDC)
    img = np.frombuffer(array, dtype='uint8')
    img.shape = (height, width, 4)
    return img
