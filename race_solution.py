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

        pass

    def read_drivers(self):#(s)
        """
            Task 2:
            Read the contents of the text file drivers.txt and return it as a single string.

            Returns: 
                str: The content of the text file as a single string
        """
        # Your code here

        pass

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
        
        pass

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

        pass

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

        pass

    def overall_table(self, results_string, drivers_string):#(s)
        """
            Task 5:
            Output the overall results table for all races.
            This is calculated by adding the points scored for each driver and placing them in order with the largest points total coming first.
        
            Parameters:
                results_string (str): The text string from Task 1
                drivers_string (str): The text string from Task 2

            Returns:
                str: The overall results table.
        """
        # Your code here

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