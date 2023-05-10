from RPA.Robocorp.WorkItems import WorkItems


def main():
    library = WorkItems()
    library.get_input_work_item()
    variables = library.get_work_item_variables()
    print('UNIQUE IDENTIFIER#1425')
    print(variables)


if __name__ == "__main__":
    main()
