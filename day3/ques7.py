def main():
    coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
    res=[x for x in coords if (x[0]>0 and x[1]>0)]
    print(res)
main()