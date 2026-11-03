root_agent = Agent(
    name="box",
    model=settings.model,
    instruction=INSTRUCTION,
    tools=[
        get_strategy,
        read_bulletin,
        FunctionTool(send_radio, require_confirmation=True),
    ],
    before_tool_callback=guard_radio,
)
