from autogen_agentchat.teams import RoundRobinGroupChat

# Agents
from agents.planner import planner_agent
from agents.researcher import researcher_agent

from utils.utils import get_termination_condition

team = RoundRobinGroupChat(
    participants=[planner_agent, researcher_agent],
    name="Travel Team",
    description="""
        A team of agents that helps users plan their trips by providing 
        information about iternaries, destinations, and travel tips.
    """,
    system_message="""
        You are a travel planning team. Your task is to help users plan their
        trips by providing information about destinations, iteranaries, and
        travel tips.
    """,
    termination_condition=get_termination_condition()
)
