import datetime

def get_timestamp():
    cur_time = datetime.datetime.now()
    file_suffix = cur_time.strftime("%Y-%m-%d-%H-%-M-%S-%f")
    return cur_time, file_suffix


def main():
    cur_time, file_suffix = get_timestamp()
    print(cur_time)
    print(file_suffix)


if __name__ == '__main__':
    main()