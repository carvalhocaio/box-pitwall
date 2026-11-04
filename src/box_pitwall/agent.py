from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from box_pitwall.guardrails import guard_radio
from box_pitwall.prompts import INSTRUCTION
from box_pitwall.settings import MODEL
from box_pitwall.tools import get_strategy, list_bulletins, read_bulletin, send_radio

root_agent = Agent(
    name="box",
    model=MODEL,
    description="Pit wall assistant of the Trench Racing team.",
    instruction=INSTRUCTION,
    tools=[
        get_strategy,
        list_bulletins,
        read_bulletin,
        FunctionTool(send_radio, require_confirmation=True),
    ],
    before_tool_callback=guard_radio,
)
