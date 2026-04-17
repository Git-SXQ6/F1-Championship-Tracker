"""
This is a stub for the COMP16321 Coding Challenge.
Do not edit or delete any lines given in this file that are marked with a "(s)".
(you can move them to different lines as long as you do not change the overall structure)

Place your code below the comments marked "#Your code here".

Each method is documented to explain what work is to be placed within it.

NOTE: You can create as many more methods as you need. However, you need to add 
self as a parameter of the new method and to call it with the prefix self.name 

EXAMPLE:

def individual_race_result(self, results_string, drivers_string, race_number):#(s)
    results_string = "1, 2, 3, 4, 5"
    single_digit = self.remove_highest_value(results_string)
    return(single_digit)

def remove_highest_value(self, results_string):
    results_string.pop(10)
    return results_string
"""


class Races:#(s)

    def read_results(self):#(s)
        """
            Task 1:
            Read the contents of the text file results.txt and return it as a single string.

            Returns: 
                str: The content of the text file as a single string
        """
        # Your code here
        with open("results.txt", "r") as file:
            results_string = file.read()
        return results_string
        pass
# # 这一段作为检查用，可以最后删掉
# if __name__ == '__main__':
#     my_instance = Races()
#     task_1 = my_instance.read_results()
#     print(task_1)

    def read_drivers(self):#(s)
        """
            Task 2:
            Read the contents of the text file drivers.txt and return it as a single string.

            Returns: 
                str: The content of the text file as a single string
        """
        # Your code here
        with open("drivers.txt", "r") as file:
            drivers_string = file.read()
        return drivers_string
        pass

# #测试内容
# if __name__ == '__main__':
#     my_instance = Races()
#     task_2 = my_instance.read_drivers()
#     print(task_2)

    def parse_drivers(self, drivers_string):
        drivers_data = {}
        lines = drivers_string.split("\n")

        for line in lines:
            if line != "":
                parts = line.split(", ")
                driver_number = int(parts[0])
                name = parts[1]
                team = parts[2]

                drivers_data[driver_number] = {
                    "name": name,
                    "team": team
                }

        return drivers_data
    
# #测试function的内容
# if __name__ == '__main__':
#     my_instance = Races()
#     drivers_string = my_instance.read_drivers()
#     drivers_data = my_instance.parse_drivers(drivers_string)
#     print(drivers_data)

    def parse_results(self, results_string):
        results_data = {}
        lines = results_string.split("\n")

        for line in lines:
            if line != "":
                parts = line.split(", ", 2)
                race_number = int(parts[0])
                driver_number = int(parts[1])
                lap_string = parts[2]

                lap_string = lap_string[1:-1]
                lap_parts = lap_string.split(", ")

                laps = []
                for item in lap_parts:
                    if item == "crashed" or item == "retired":
                        laps.append(item)
                    else:
                        laps.append(float(item))

                if race_number not in results_data:
                    results_data[race_number] = {}

                results_data[race_number][driver_number] = laps

        return results_data

#检查的内容
# if __name__ == '__main__':
#     my_instance = Races()
#     results_string = my_instance.read_results()
#     results_data = my_instance.parse_results(results_string)
#     print(results_data)



    def analyse_laps(self, laps):
        total_time = 0
        completed_laps = 0

        for i in range(len(laps)):
            item = laps[i]

            if item == "crashed" or item == "retired":
                return {
                    "status": item,
                    "total_time": None,
                    "completed_laps": completed_laps,
                    "incident_lap": i + 1,
                    "previous_time": total_time
                }
            else:
                total_time += item
                completed_laps += 1

        return {
            "status": "finished",
            "total_time": total_time,
            "completed_laps": completed_laps,
            "incident_lap": None,
            "previous_time": total_time
        }

# 检查analyse laps
# if __name__ == '__main__':
#     my_instance = Races()
#     results_string = my_instance.read_results()
#     results_data = my_instance.parse_results(results_string)
#     print(my_instance.analyse_laps(results_data[1][1]))
#     print(my_instance.analyse_laps(results_data[1][12]))
#     print(my_instance.analyse_laps(results_data[2][7]))

    def position_suffix(self, position):
        if position == 1:
            return "1st"
        elif position == 2:
            return "2nd"
        elif position == 3:
            return "3rd"
        else:
            return f"{position}th"


    def individual_race_result(self, results_string, drivers_string, race_number):#(s)
        """
            Task 3:
            Calculate and Output the results of a specified race. Where the race to be outputted is given by the automarker.
            This method determines the results of a specific race which is denoted by the "race_number" parameter. The winner is the driver with the lowest overall time for completing the race.
            If a driver crashes or retires their position will be determined by which lap this happens on.
        
            Parameters:
                results_string (str): The text string from Task 1
                drivers_string (str): The text string from Task 2
                race_number (int): An integer denoting which race's results to be calculated

            Returns:
                str: The results from the specified race.
        """
        # Your code here
        drivers_data = self.parse_drivers(drivers_string)
        results_data = self.parse_results(results_string)

        if race_number not in results_data:
            return f"No Results Available for Race {race_number}"

        race_results = []

        for driver_number in results_data[race_number]:
            name = drivers_data[driver_number]["name"]
            laps = results_data[race_number][driver_number]
            analysis = self.analyse_laps(laps)

            race_results.append({
                "driver_number": driver_number,
                "name": name,
                "analysis": analysis
            })

        finished = []
        not_finished = []

        for result in race_results:
            if result["analysis"]["status"] == "finished":
                finished.append(result)
            else:
                not_finished.append(result)

        # Finished drivers: lowest total time first
        finished.sort(key=lambda x: x["analysis"]["total_time"])

        # Crashed / retired drivers:
        # later incident lap comes first
        # if same incident lap, lower previous_time comes first
        # if both crashed/retired on lap 1, alphabetical order decides
        not_finished.sort(
            key=lambda x: (
                -x["analysis"]["incident_lap"],
                x["analysis"]["previous_time"],
                x["name"]
            )
        )

        final_order = finished + not_finished

        points_list = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

        output_parts = []

        for i in range(len(final_order)):
            position = i + 1
            result = final_order[i]
            name = result["name"]

            if result["analysis"]["status"] == "finished" and i < 10:
                points = points_list[i]
            else:
                points = 0

            position_text = self.position_suffix(position)
            output_parts.append(f"{position_text} {name} {points}pts")

        return f"Results from Race {race_number}: " + ", ".join(output_parts)

# if __name__ == '__main__':
#     my_instance = Races()
#     results_string = my_instance.read_results()
#     drivers_string = my_instance.read_drivers()

#     print(my_instance.individual_race_result(results_string, drivers_string, 1))
#     print(my_instance.individual_race_result(results_string, drivers_string, 2))
#     print(my_instance.individual_race_result(results_string, drivers_string, 3))


    def driver_in_race_result(self, results_string, drivers_string, race_number, driver_number):#(s)
        """
            Task 4:
            Output the results of a specified driver for a specified race. Where the driver and race to be outputted is given by the automarker.
            This method determines the results for a certain drivers in a specific race where the driver is denoted by "driver_number" and race by the "race_number"
        
            Parameters:
                results_string (str): The text string from Task 1
                drivers_string (str): The text string from Task 2
                race_number (int): An integer denoting which race's results to use
                driver_number (int): An integer denoting which drivers details to use

            Returns:
                str: The specific drivers race result.
        """

        # Your code here
        drivers_data = self.parse_drivers(drivers_string)
        results_data = self.parse_results(results_string)

        if race_number not in results_data:
            return f"No Results Available for Race {race_number}"

        if driver_number not in results_data[race_number]:
            return f"No Results Available for Driver {driver_number}, Race {race_number}"

        name = drivers_data[driver_number]["name"]
        team = drivers_data[driver_number]["team"]
        laps = results_data[race_number][driver_number]
        analysis = self.analyse_laps(laps)

        if analysis["status"] == "finished":
            total_time = analysis["total_time"]
            minutes = int(total_time // 60)
            seconds = int(total_time % 60)
            return f"Results for Driver {driver_number}, Race {race_number}: {name}, {team}, {minutes}mins {seconds}secs"

        elif analysis["status"] == "crashed":
            return f"Results for Driver {driver_number}, Race {race_number}: {name}, {team}, Crashed"

        elif analysis["status"] == "retired":
            return f"Results for Driver {driver_number}, Race {race_number}: {name}, {team}, Retired"


# #检查
# if __name__ == '__main__':
#     my_instance = Races()
#     results_string = my_instance.read_results()
#     drivers_string = my_instance.read_drivers()

#     print(my_instance.driver_in_race_result(results_string, drivers_string, 1, 15))
#     print(my_instance.driver_in_race_result(results_string, drivers_string, 1, 25))
#     print(my_instance.driver_in_race_result(results_string, drivers_string, 1, 12))
#     print(my_instance.driver_in_race_result(results_string, drivers_string, 3, 15))
#     print(my_instance.driver_in_race_result(results_string, drivers_string, 1, 99))

    def average_lap_times(self, results_string, drivers_string, race_number, driver_number):#(s)
        """
            Task 5:
            Output the average lap time for a specified driver to 2dp in a given race where both the driver number and race number is provided.
            The race number will be from 0-x where x is the final race in the input file. For example if race number = 2 then you provide the average lap time for the second race.
            If the race number provide is 0 then you should calculate their average lap time across every race.
        
            Parameters:
                results_string (str): The text string from Task 1
                drivers_string (str): The text string from Task 2
                race_number (int): The race number for the lap times to be averaged
                driver_number (int): The driver to be considered in the calculation

            Returns:
                float: The average lap times for the specified driver
                str: The relevant message if average lap time not appropriate
        """

        # Your code here
        results_data = self.parse_results(results_string)
        lap_times = []

        if race_number == 0:
            for race in results_data:
                if driver_number in results_data[race]:
                    laps = results_data[race][driver_number]
                    for item in laps:
                        if type(item) == float:
                            lap_times.append(item)
        else:
            laps = results_data[race_number][driver_number]
            for item in laps:
                if type(item) == float:
                    lap_times.append(item)

        if len(lap_times) == 0:
            return "No Average Lap Time Available"

        average = sum(lap_times) / len(lap_times)
        return round(average, 2)

# #检查
# if __name__ == '__main__':
#     my_instance = Races()
#     results_string = my_instance.read_results()
#     drivers_string = my_instance.read_drivers()
    
#     print(my_instance.average_lap_times(results_string, drivers_string, 1, 15))
#     print(my_instance.average_lap_times(results_string, drivers_string, 2, 7))
#     print(my_instance.average_lap_times(results_string, drivers_string, 0, 15))


    def overall_table(self, results_string, drivers_string):#(s)
        """
            Task 6:
            Output the overall results table for all races.
            This is calculated by adding the points scored for each driver and placing them in order with the largest points total coming first.
        
            Parameters:
                results_string (str): The text string from Task 1
                drivers_string (str): The text string from Task 2

            Returns:
                str: The overall results table.
        """
        # Your code here
        drivers_data = self.parse_drivers(drivers_string)
        results_data = self.parse_results(results_string)

    points_list = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

    overall_stats = {}

    # initialize all drivers
    for driver_number in drivers_data:
        overall_stats[driver_number] = {
            "name": drivers_data[driver_number]["name"],
            "team": drivers_data[driver_number]["team"],
            "points": 0,
            "positions": {}
        }

    # process each race
    for race_number in results_data:
        race_results = []

        for driver_number in results_data[race_number]:
            name = drivers_data[driver_number]["name"]
            laps = results_data[race_number][driver_number]
            analysis = self.analyse_laps(laps)

            race_results.append({
                "driver_number": driver_number,
                "name": name,
                "analysis": analysis
            })

        finished = []
        not_finished = []

        for result in race_results:
            if result["analysis"]["status"] == "finished":
                finished.append(result)
            else:
                not_finished.append(result)

        finished.sort(key=lambda x: x["analysis"]["total_time"])
        not_finished.sort(
            key=lambda x: (
                -x["analysis"]["incident_lap"],
                x["analysis"]["previous_time"],
                x["name"]
            )
        )

        final_order = finished + not_finished

        for i in range(len(final_order)):
            position = i + 1
            driver_number = final_order[i]["driver_number"]
            status = final_order[i]["analysis"]["status"]

            # record finishing position count for tie-break
            if position not in overall_stats[driver_number]["positions"]:
                overall_stats[driver_number]["positions"][position] = 0
            overall_stats[driver_number]["positions"][position] += 1

            # assign points only if finished and top 10
            if status == "finished" and i < 10:
                overall_stats[driver_number]["points"] += points_list[i]

    # sort overall table
    overall_list = list(overall_stats.values())

    def sort_key(driver):
        key = [-driver["points"]]

        # compare counts of 1st, 2nd, 3rd ... up to last place
        for pos in range(1, len(drivers_data) + 1):
            key.append(-driver["positions"].get(pos, 0))

        key.append(driver["name"])
        return tuple(key)

    overall_list.sort(key=sort_key)

    output_parts = []

    for i in range(len(overall_list)):
        position_text = self.position_suffix(i + 1)
        driver = overall_list[i]
        output_parts.append(
            f"{position_text} {driver['name']} {driver['team']} {driver['points']}pts"
        )

    return "Overall Results: " + ", ".join(output_parts)
        pass

    

if __name__ == '__main__':
    # You can place any ad-hoc testing here
    # my_instance = Races()
    # task_1 = my_instance.read_results()
    # print(task_1)

    # task_2 = my_instance.read_drivers()
    # print(task_2)

    # task_3 = my_instance.read_drivers(task_1, task_2, 1)
    # print(task_3)

    pass

