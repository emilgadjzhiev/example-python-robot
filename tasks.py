import time

import requests
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


def simulate_robot_work(config, duration):  # do whatever with config
    time.sleep(duration)


def simulate_robot_failure(robot_id):
    # POST failure to Robot API

    payload = {
        "error": "Can't connect to the Epic.",
        "error_type": "epic_error"
    }
    requests.post(f'http://127.0.0.1:7000/robot/process/{robot_id}/terminate', data=payload)


def simulate_robot_finish(robot_id):
    # POST finish to Robot API

    payload = {
        "activities_processed": 50,
        "number_of_exceptions": 50
    }
    requests.post(f'http://127.0.0.1:7000/robot/process/{robot_id}/finish', data=payload)


def main():
    variables = get_robot_variables()
    robot_id = variables['robot_id']
    work_duration = variables['work_duration']
    finish_result = variables['finish_result']

    config = retrieve_robot_configuration(robot_id)
    if finish_result == 'failure':
        simulate_robot_failure(robot_id)
    simulate_robot_work(config, work_duration)
    simulate_robot_finish(robot_id)


if __name__ == "__main__":
    main()
