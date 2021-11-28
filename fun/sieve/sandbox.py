from reduced_residue_system import ancestors_compositeness, random_rrsp


def main():
    depth = 80
    counts = [0 for _ in range(depth)]
    for i in range(1000):
        for j, is_composite in enumerate(
                ancestors_compositeness(random_rrsp(depth))):
            if is_composite:
                counts[j] += 1
        print(i, counts)


if __name__ == '__main__':
    main()
