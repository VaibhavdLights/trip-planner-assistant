import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools import tool

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
	model="gemini-1.5-flash",
	verbose=True,
	temperature=0.5,
	google_api_key=os.getenv("GOOGLE_API_KEY"),
)

@CrewBase
class TripPlannerAssistantCrew():
	"""TripPlannerAssistant crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			llm=llm,
			tools=[tool],
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=llm,
   			tools=[tool],
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
   			tools=[tool],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
   			tools=[tool],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TripPlannerAssistant crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)