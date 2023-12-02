def try_generator():
    for data in (1, 2, 3, 4, 5):
        yield data


def main():
    # for data in try_generator():
    for data in (data for data in (1, 2, 3, 4, 5)):
        print(data)
        if data > 2:
            break


print(main())
