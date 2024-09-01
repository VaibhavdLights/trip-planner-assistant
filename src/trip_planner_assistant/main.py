#!/usr/bin/env python
import sys
from trip_planner_assistant.crew import TripPlannerAssistantCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'origin': origin,
        'destination': destination,
        'date_range': date_range,
        'interests': interests,
    }
    TripPlannerAssistantCrew().crew().kickoff(inputs=inputs)

if __name__ == '__main__':
    print("-----Enter Details To Plan Travel Itienary-----")
    print("-----#####################################-----")
    origin=input('Enter Origin City/Country ->> ')
    destination=input('Enter Destination City/Country ->> ')
    date_range=input('Enter Date Range ->> ')
    interests=input('Enter Interests ->> ')

    run()