import logging
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages

from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    RoomInputOptions,
    WorkerOptions,
    cli,
)
from livekit.plugins import langchain, silero
from livekit.plugins import openai, silero

logger = logging.getLogger("basic-agent")

load_dotenv()

# this example demonstrates adding Voice to a LangGraph graph by using our
# adapter.
# In this example, instructions and tool calls are handled in LangGraph, while
# voice orchestration (turns, interruptions, etc) are handled by Agents framework
# In order to run this example, you need the following dependencies
# - langchain[openai]
# - langgraph
# - livekit-agents[openai,silero,langchain,deepgram,turn_detector]


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# a simple StateGraph with a single GPT-4o node
def create_graph() -> StateGraph:
    openai_llm = init_chat_model(
        model="gpt-4o-mini",
    )

    def chatbot_node(state: State):
        return {"messages": [openai_llm.invoke(state["messages"])]}

    builder = StateGraph(State)
    builder.add_node("chatbot", chatbot_node)
    builder.add_edge(START, "chatbot")
    return builder.compile()


async def entrypoint(ctx: JobContext):
    graph = create_graph()

    agent = Agent(
        instructions="",
        llm=langchain.LLMAdapter(graph),
    )

    session = AgentSession(
        vad=silero.VAD.load(),
        # any combination of STT, LLM, TTS, or realtime API can be used
        stt=openai.STT(model="gpt-4o-mini-transcribe"),
        tts=openai.TTS(model="gpt-4o-mini-tts"),
    )

    await session.start(
        agent=agent,
        room=ctx.room
    )
    await session.generate_reply(instructions="ask the user how they are doing?")


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))