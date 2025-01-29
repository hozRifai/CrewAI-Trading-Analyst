from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

load_dotenv()

@CrewBase
class AiLatestDevelopment():
	"""AiLatestDevelopment crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def lead_market_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['lead_market_analyst'],
			verbose=True
		)

	@agent
	def chief_marketing_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['chief_marketing_strategist'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AiLatestDevelopment crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
