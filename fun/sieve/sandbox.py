from reduced_residue_system import ancestors_compositeness, random_rrsp


def main():
    counts = [0 for _ in range(80)]
    for i in range(10):
        for j, is_composite in enumerate(
                ancestors_compositeness(random_rrsp(80))):
            if is_composite:
                counts[j] += 1
        print(i, counts)


if __name__ == '__main__':
    main()
