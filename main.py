import random


class Rod:
    WOOD_ROD = 1
    ALUMINUM_ROD = 2


class Bait:
    WORM = 1
    SHRIMP = 2


class Fish:
    GOLDEN_FISH = 1
    SALMON = 2
    SHARK = 3
    CRAB = 4


class Fisher:
    def __init__(self, rod=Rod.WOOD_ROD, bait=Bait.WORM):
        self.rod = rod
        self.bait = bait

    def _run_fishing(self, golden_random_min, golden_random_max, salmon_random_min, salmon_random_max, shark_random_min, shark_random_max, crab_random_min, crab_random_max):
        random_num = int(random.random() * 100)
        if golden_random_min <= random_num <= golden_random_max:
            print('You get Golden Fish')
        elif salmon_random_min <= random_num <= salmon_random_max:
            print('You get Salmon')
        elif shark_random_min <= random_num <= shark_random_max:
            print('You get Shark')
        elif crab_random_min <= random_num <= crab_random_max:
            print('You get Crab')
        else:
            print('Error')
            print(f'random_num:{random_num}')

    def fishing(self):
        golden_random_min = 1
        golden_random_max = 11
        salmon_random_min = 12
        salmon_random_max = 30
        shark_random_min = 31
        shark_random_max = 60
        crab_random_min = 61
        crab_random_max = 100


        if self.rod == Rod.WOOD_ROD and self.bait == Bait.WORM:
            self._run_fishing(golden_random_min, golden_random_max, salmon_random_min, salmon_random_max, shark_random_min, shark_random_max, crab_random_min, crab_random_max)
        elif self.rod == Rod.ALUMINUM_ROD and self.bait == Bait.WORM:
            self._run_fishing(golden_random_min, golden_random_max, salmon_random_min, salmon_random_max, shark_random_min, shark_random_max, crab_random_min, crab_random_max)
        elif self.rod == Rod.WOOD_ROD and self.bait == Bait.SHRIMP:
            self._run_fishing(golden_random_min, golden_random_max, salmon_random_min, salmon_random_max, shark_random_min, shark_random_max, crab_random_min, crab_random_max)
        elif self.rod == Rod.ALUMINUM_ROD and self.bait == Bait.SHRIMP:
            self._run_fishing(golden_random_min, golden_random_max, salmon_random_min, salmon_random_max, shark_random_min, shark_random_max, crab_random_min, crab_random_max)
        else:
            print('Not using rod or not using bait')


if __name__ == '__main__':
    fisher = Fisher()
    fisher.fishing()

    # golden_rate = int(input('請輸入金魚出現機率'))
    # salmon_rate = int(input('請輸入鮭魚出現機率'))
    # shark_rate = int(input('請輸入鯊魚出現機率'))
    # crab_rate = int(input('請輸入螃蟹出現機率'))
    # print('轉換的八個數字為')
    # golden_random_min = 1
    # golden_random_max = golden_rate
    # salmon_random_min = golden_rate+1
    # salmon_random_max = golden_rate+salmon_rate
    # shark_random_min = golden_rate+salmon_rate+1
    # shark_random_max = golden_rate+salmon_rate+shark_rate
    # crab_random_min = golden_rate+salmon_rate+shark_rate+1
    # crab_random_max = 100
    #
    # print(f'golden_random_min={golden_random_min}')
    # print(f'golden_random_max={golden_random_max}')
    # print(f'salmon_random_min={salmon_random_min}')
    # print(f'salmon_random_max={salmon_random_max}')
    # print(f'shark_random_min={shark_random_min}')
    # print(f'shark_random_max={shark_random_max}')
    # print(f'crab_random_min={crab_random_min}')
    # print(f'crab_random_max={crab_random_max}')


