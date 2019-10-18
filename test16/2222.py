import multiprocessing


def save(aa):
    print(aa)


def main():
    urls = ['aaa', 'bbbb', 'cccc']
    p = multiprocessing.Pool(processes=4)
    for url in urls:
        p.apply_async(save, args=(url,))
    p.close()
    p.join()


if __name__ == '__main__':
    main()