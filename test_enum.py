from enum import Enum


class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3


def act_shingou(color: int) -> Shingou:
    if color not in [data.value for data in Shingou]:
        print("信号機の色に対応していません")
        return

    if color is Shingou.RED.value:
        print("とまれ")

    if color is Shingou.BLUE.value:
        print("すすめ")

    if color is Shingou.YELLOW.value:
        print("ちゅうい")

    return Shingou(color)


print(act_shingou(1))
