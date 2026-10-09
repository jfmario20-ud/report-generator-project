"""
Squadron Activity Report Generator

This script demonstrates how to use the report_functions module
to generate a comprehensive squadron activity report.

Students will build this step-by-step in the assignment.
"""

import report_functions as rf


def generate_squadron_report(squadron_code, output_file):
    """
    Generates a comprehensive activity report for a specific squadron.
    
    Args:
        squadron_code (str): Squadron identifier (e.g., 'VFA-41')
        output_file (str): Path to save the report
    """
    # TODO: PART 1 - Load the data files
    aircraft = rf.read_csv_file("data/aircraft.csv") 
    print(f"Loaded {rf.count_records(aircraft)} aircraft records.")
    flight_logs = rf.read_csv_file("data/flight_logs.csv")
    print(f"Loaded {rf.count_records(flight_logs)} flight logs.")
    pilots = rf.read_csv_file("data/pilots.csv")
    print(f"Loaded {rf.count_records(pilots)} pilot records.")

    # TODO: PART 2 - Filter data for the specified squadron
    aircraft_in_squadron = rf.filter_by_field(aircraft, "squadron", squadron_code)
    print(f"Found {rf.count_records(aircraft_in_squadron)} aircraft in squadron {squadron_code}.")
    pilots_in_squadron = rf.filter_by_field(pilots, "squadron", squadron_code)
    print(f"Found {rf.count_records(pilots_in_squadron)} pilots insquadron {squadron_code}.")
    
    
    # TODO: PART 3 - Get flights for squadron pilots
    flight_logs_for_squadron = []
    for pilot in pilots_in_squadron:
        pilot_id = pilot["pilot_id"]
        pilot_flights = rf.filter_by_field(flight_logs, "pilot_id", pilot_id)
        flight_logs_for_squadron.extend(pilot_flights) 
    print(f"Found {rf.count_records(flight_logs_for_squadron)} flight logs for squadron {squadron_code}.")

    # TODO: PART 4 - Calculate statistics
    total_flights = rf.count_records(flight_logs)
    print(f"Total flights: {total_flights}") 
    total_flight_hours = rf.calculate_total(aircraft, "total_flight_hours")
    print(f"Total flight hours: {total_flight_hours}")  
    average_flight_hours = rf.calculate_average(aircraft, "total_flight_hours")
    print(f"Average flight hours per aircraft: {average_flight_hours:.2f}") 

    # TODO: PART 5 - Build the report content
    report_content = f"Squadron Activity Report for {squadron_code}\n"
    report_content += f"Total Aircraft: {rf.count_records(aircraft_in_squadron)}\n"
    report_content += f"Total Pilots: {rf.count_records(pilots_in_squadron)}\n"
    report_content += f"Total Flights: {rf.count_records(flight_logs_for_squadron)}\n"
    report_content += f"Total Flight Hours: {total_flight_hours}\n"
    report_content += f"Average Flight Hours per Aircraft: {average_flight_hours:.2f}\n"

    # TODO: PART 6 - Write the report to file
    rf.write_report_to_file(output_file, report_content) 


# Main execution
if __name__ == '__main__':
    # TODO: Students will customize this to generate reports for different squadrons
    print("Generating squadron activity reports...")
    
    # Example: Generate report for VFA-41 (Black Aces)
    generate_squadron_report('VFA-41', '../reports/vfa-41-report.txt')
    
    print("\nImplement the function above, then uncomment to test!")
