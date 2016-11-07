import itertools

def main():
    perms = list(itertools.permutations(range(10)))
    perms = list(sorted(perms))
    return perms

if __name__ == '__main__':
    main()
