import pathlib


def export_two_arr(list_1, lis_2, file_name, folder):
    # main_path = f"D:\\DEVELOP PROJECTS\\В рамках предмета в универе\\dynamic-systems\\{folder}\\"
    main_path = pathlib.Path(__file__).parent.resolve()


    line = ""
    file = open(f'{main_path}/{folder}/{file_name}.txt', 'w')
    for x, y in zip(list_1, lis_2):
        line += f"{x} {y}\n"

    file.write(line)
