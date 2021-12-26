import akpy.util

def main():
    a = akpy.util.Accumulator()
    a.append(**{'a': 1, 'b': 2})
    print(a.get_dict_numpy())

if __name__ == '__main__':
    main()


