#!/usr/bin/env python
import sys
from trip_planner_assistant.crew import TripPlannerAssistantCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs'
    }
    TripPlannerAssistantCrew().crew().kickoff(inputs=inputs)