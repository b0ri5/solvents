from reduced_residue_system import *

import graphviz


def main():
    dot = graphviz.Digraph(comment='A tree of twin primes')
    dot.node(2)


if __name__ == '__main__':
    main()
