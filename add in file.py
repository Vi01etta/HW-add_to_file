import glob
read_files = glob.glob("*.txt")


main_list = []

for f in read_files:
      with open(f, "r", encoding='utf-8') as infile:
            text = infile.readlines()
            infile.seek(0)
            num_of_lines = len(text)
            tuple_list = (f, str(num_of_lines), infile.read())
            main_list.append(tuple_list)





with open('result.txt', "w") as outfile:
    sorted_list = sorted(main_list, key=lambda tup: tup[1])
    for tuple_values in sorted_list:
        for text_values in tuple_values:
            outfile.write(text_values)
            outfile.write('\n')
    

