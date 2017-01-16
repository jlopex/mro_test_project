import time


class MROApi(object):

    def print_smthg(self, i):
        print("TEST {}: {}".format(self.smthg, i))
        time.sleep(1)

    def run(self):
        print("HELLO")

        for i in xrange(10):
            self.print_smthg(i)

    def __init__(self, smthg):
        self.smthg = smthg


def main():
    MROApi("JRD").run()

if __name__ == '__main__':
    main()
