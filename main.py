import distances
def main_program():
    main_menu = input("What do you want to do?\n[0]: Exit program\n[1]: Load trucks\n[2]: Lookup a package")

    if main_menu == "0":
        print("0 was pressed")

    elif main_menu == "1":
        print("1 was pressed")
        wgups_graph.get_distance_data("wgups_distances.csv")


    elif main_menu == "2":
        print("2 was pressed")

    else:
        print("Invalid key was pressed. Try again.")
        main_program()


main_program()
