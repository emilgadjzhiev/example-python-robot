import time

from RPA.Robocorp.WorkItems import WorkItems


def get_robot_variables():
    """
    Variables example:
    {
        'robot_id': 4,
        'work_duration': 10,
        'finish_result': 'failure'
    }
    """
    library = WorkItems()
    library.get_input_work_item()
    return library.get_work_item_variables()

def retrieve_robot_configuration(robot_id) -> dict:
    config = {}  # get robot config -> GET to Robot API
    return config


def simulate_robot_work(config, duration): # do whatever with config
    time.sleep(duration)


def simulate_robot_failure():
    # POST failure to Robot API
    pass

def simulate_robot_finish():
    # POST finish to Robot API
    pass


def main():
    variables = get_robot_variables()
    config = retrieve_robot_configuration(variables['robot_id'])
    if variables['finish_result'] == 'failure':
        simulate_robot_failure()
    simulate_robot_work(config, variables['work_duration'])
    simulate_robot_finish()


if __name__ == "__main__":
    main()
