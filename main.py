# Stephon Patton ID: 005884992
from datetime import datetime
import time

import distances
import package
from truck import simulate_package_delivery, load_all_trucks, truck1, truck3, truck2, show_packages_at_time, \
    show_metrics, deliver_package, mark_as_delivered
from package import package_hashtable
from greedy_algorithm import greedy_algorithm


def main_program():
    end_of_day_status = datetime(2022, 1, 10, 14, 00)

    combined_distance = truck1.total_distance + truck2.total_distance + truck3.total_distance
    # show_packages_at_time(test_time)
    main_menu = input(
        "What do you want to do?\n[0]: Exit program\n[1]: Load trucks")

    if main_menu == "0":
        quit()

    elif main_menu == "1":
        if len(truck1.packages) > 0:
            print("Already loaded..")
            time.sleep(1.0)
            sub_menu = input("What would you like to do now?\n[0]: Exit Program\n[1]: Package Status #1 (8:35 & 9:25)\n")
            secondary_menu(sub_menu, '233 Canyon Rd', end_of_day_status, False)
        else:
            print("Loading trucks...")
            time.sleep(1.0)
            print("Trucks loaded!")
            load_all_trucks()
            sub_menu = input("What would you like to do now?\n[0]: Exit Program\n[1]: Package Status #1 (8:35 & 9:25)\n")
            last_stop = truck2.route[0]
            simulate_package_delivery()
            secondary_menu(sub_menu, last_stop, end_of_day_status, False)

    else:
        print("Invalid key was pressed. Try again.")
        main_program()


def secondary_menu(sub_menu, last_stop, end_of_day_status, address_fixed):
    if sub_menu == "1":
        check_time = input("Please enter a time in the format (HH:mm)")
        testing = check_time.split(':')
        if not testing[0].isnumeric() or not testing[1].isnumeric() or int(testing[0]) > 24 or int(testing[0]) < 8 \
                or int(testing[1]) > 60 or int(testing[1]) < 0:
            print("Invalid format or numbers provided. Try again.")
            secondary_menu(sub_menu, last_stop, end_of_day_status, False)
        elif int(testing[0]) > 9:
            print("Time out of status #1 hour range")
            secondary_menu(sub_menu, last_stop, end_of_day_status, False)
        else:
            hour = testing[0]
            mins = testing[1]
            status_1 = datetime(2022, 1, 10, int(hour), int(mins))
            show_packages_at_time(status_1)


        if not address_fixed:
            time.sleep(3)
            fix = input("\nATTENTION: IT IS 10:25 and package 9 needs an address fix. "
                        "\nFix package 9? Enter y for yes, n for no")
            # TODO: Add custom time for each status check and make sure it works... after dinner
            if fix == 'y':
                for pack in truck2.packages:
                    if pack[0] == 9:
                        truck2.remove(pack)
                updated_pack = [9, '410 S State St', 'Salt Lake City', 'UT', '84111', '17:00', 9, '', 'En Route', '2',
                                '']
                truck2.load_package(updated_pack)
                package_hashtable.insert(9, updated_pack)
                truck2.route = greedy_algorithm(truck2.route)
                truck2.route.pop(0)
                truck2.route.append('4001 South 700 East')
                deliver_time = deliver_package(last_stop, truck2.route[0], truck2)
                mark_as_delivered(updated_pack, deliver_time)
                truck2.current_time = deliver_time
                deliver_time = deliver_package(truck2.route[0], truck2.route[1], truck2)
                truck2.end_time = deliver_time
                time.sleep(1)
                print("Address fixed!")
            else:
                print("Can't proceed without fixing address.. exiting system")
                quit()
    else:
        print("Try again")
        main_program()

    sub_menu = input("What would you like to do now?\n[0]: Exit Program\n[1]: Package Status #2 (9:35 & 10:25)\n")
    if sub_menu == '1':
        check_time = input("Please enter a time in the format (HH:mm)")
        testing = check_time.split(':')
        if not testing[0].isnumeric() or not testing[1].isnumeric() or int(testing[0]) > 24 or int(testing[0]) < 8 \
                or int(testing[1]) > 60 or int(testing[1]) < 0:
            print("Invalid format or numbers provided. Try again.")
            secondary_menu(sub_menu, last_stop, end_of_day_status, True)
        elif int(testing[0]) > 10:
            print("Time out of status #2 hour range")
            secondary_menu(sub_menu, last_stop, end_of_day_status, True)
        else:
            hour = testing[0]
            mins = testing[1]
            status_2 = datetime(2022, 1, 10, int(hour), int(mins))
            show_packages_at_time(status_2)
    else:
        print("Try again")
        secondary_menu(sub_menu, last_stop, end_of_day_status, True)


    sub_menu = input("What would you like to do now?\n[0]: Exit Program\n[1]: Package Status #3 (12:03 & 1:12)\n")
    if sub_menu == '1':
        check_time = input("Please enter a time in the format (HH:mm)")
        testing = check_time.split(':')
        if not testing[0].isnumeric() or not testing[1].isnumeric() or int(testing[0]) > 24 or int(testing[0]) < 8 \
                or int(testing[1]) > 60 or int(testing[1]) < 0:
            print("Invalid format or numbers provided. Try again.")
            secondary_menu(sub_menu, last_stop, end_of_day_status, True)
        elif int(testing[0]) > 13:
            print("Time out of status #1 hour range")
            secondary_menu(sub_menu, last_stop, end_of_day_status, True)
        else:
            hour = testing[0]
            mins = testing[1]
            status_3 = datetime(2022, 1, 10, int(hour), int(mins))
            show_packages_at_time(status_3)
    else:
        print("Try again")
        secondary_menu(sub_menu, last_stop, end_of_day_status, True)

    sub_menu = input("What would you like to do now?\n[0]: Exit Program\n[1]: View all packages at the end of the "
                     "day")
    if sub_menu == '1':
        show_packages_at_time(end_of_day_status)
    else:
        print("Invalid key pressed. Exiting...")
        quit()

    sub_menu = input("What would you like to do now?\n[0]: Exit Program\n[1]: View trucks totals")
    if sub_menu == '1':
        show_metrics(truck1.total_distance, truck2.total_distance, truck3.total_distance)
    else:
        print("Invalid key pressed. Exiting...")
        quit()

    sub_menu = input("Would you like to view all package data or would you like to exit program? y for yes, "
                     "n for no")
    if sub_menu == 'y':
        package.print_all()
        time.sleep(2)
        print("Thank you for using WGUPS system! Have a good day.")
        quit()
    else:
        print("Invalid key pressed. Exiting...")
        quit()


main_program()
