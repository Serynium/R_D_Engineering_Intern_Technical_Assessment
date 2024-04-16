def main(n: int) -> None:
    for row in range(1, n + 1):
        print(f"{' ' * (n - row)}{' #' * row}")


if __name__ == "__main__":
    main(n=4)