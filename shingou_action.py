from enum import Enum
import sys


class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3


args = sys.argv


def act_shingou() -> Shingou:
    args1 = int(args[1])

    if args1 not in [data.value for data in Shingou]:
        print("信号機の色に対応していません")

    if args1 is Shingou.RED.value:
        print("とまれ")

    if args1 is Shingou.BLUE.value:
        print("すすめ")

    if args1 is Shingou.YELLOW.value:
        print("ちゅうい")

    return Shingou(args1)


print(act_shingou())
