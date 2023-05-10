from RPA.Robocorp.WorkItems import WorkItems


def main():
    library = WorkItems()
    library.get_input_work_item()
    variables = library.get_work_item_variables()
    print(f'Robot id: {variables["robot_id"]}')


if __name__ == "__main__":
    main()
