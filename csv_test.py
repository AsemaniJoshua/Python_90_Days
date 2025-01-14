import csv

# with open("names.csv","r") as file:
#     readed_file = csv.reader(file)
#
#     # skips the first line
#     # next(readed_file)
#     #
#
#     with open("new_names.csv", "w") as new_file:
#         writer = csv.writer(new_file, delimiter=",")
#         for row in readed_file:
#             # print(row[2])
#             writer.writerow(row)

with open("names.csv","r") as file:
    readed_file = csv.DictReader(file)
    # for line in readed_file:
    #     print(line.get("Email"))
    with open("new_names.csv", "w") as new_file:
        fieldnames = ["first_name", "last_name", "Email"]
        write_to_file = csv.DictWriter(new_file,fieldnames=fieldnames, delimiter="\t")
        write_to_file.writeheader()
        for line in readed_file:
            write_to_file.writerow(line)


