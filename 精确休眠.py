import time

'''
通用
'''
def accurate_delay(delay):
    '''
    毫秒级精确休眠
    '''
    _ = time.perf_counter() + delay / 1000
    while time.perf_counter() < _:
        # pass 直接pass可能会更多地占用cpu造成阻塞 但是会更精准

        '''
        一些不耗时操作
        '''
        d = {}
        d.update()
        del d


'''
linux平台   patch time.sleep
'''
import time
from ctypes import cdll

glibc = None


def _custom_sleep(t):
    glibc.usleep(int(t * 1000000))


def patch_time():
    global glibc
    try:
        glibc = cdll.LoadLibrary("libc.so.6")

        time.sleep = _custom_sleep
    except Exception as e:
        print(f"Failed to patch time.sleep: {e}. Performance might be worse.")


patch_time()
