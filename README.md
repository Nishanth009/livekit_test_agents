# livekit_test_agents
A repo to experiment with livekit agents <br>

# step 1: run live kit server 
INSTALL LIVEKIT AND RUN<br>
livekit-server --dev  <br>

# step 2: install agents
pip install "livekit-agents[openai,silero,deepgram,cartesia,turn-detector, langgraph]~=1.0"<br>
export LIVEKIT_URL="ws://localhost:7880"<br>
export LIVEKIT_API_KEY="devkey"<br>
export LIVEKIT_API_SECRET="secret"<br>
python voice_agent_langgraph.py start<br>

# step 3: React webpage
git clone https://github.com/livekit-examples/agent-starter-react/tree/main?tab=readme-ov-file<br>
cd to react agent started folder<br>
export LIVEKIT_URL="ws://localhost:7880"<br>
export LIVEKIT_API_KEY="devkey"<br>
export LIVEKIT_API_SECRET="secret"<br>
pnpm install<br>
pnpm dev<br>

RUN all in different terminals at once <br>

