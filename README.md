# livekit_test_agents
A repo to experiment with livekit agents

# step 1: run live kit server
INSTALL LIVEKIT AND RUN
livekit-server --dev  

# step 2: install agents
pip install "livekit-agents[openai,silero,deepgram,cartesia,turn-detector, langgraph]~=1.0"
export LIVEKIT_URL="ws://localhost:7880"
export LIVEKIT_API_KEY="devkey"
export LIVEKIT_API_SECRET="secret"
python voice_agent_langgraph.py start

# step 3: React webpage
git clone https://github.com/livekit-examples/agent-starter-react/tree/main?tab=readme-ov-file
cd to react agent started folder
export LIVEKIT_URL="ws://localhost:7880"
export LIVEKIT_API_KEY="devkey"
export LIVEKIT_API_SECRET="secret"
pnpm install
pnpm dev

RUN all in different terminals at once 

