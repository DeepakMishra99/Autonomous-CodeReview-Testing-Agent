<body>

<header>
    <h1>🤖 Autonomous Code Agent</h1>
</header>

<div class="container">
    <div class="card">
        <h2>✨ Overview</h2>
        <p>Autonomous Code Agent is an agentic workflow built with <strong>LangGraph</strong> and <strong>gemini-3.1-flash-lite-preview</strong> that automates the entire software development lifecycle. It doesn't just write code; it reviews its own work, generates unit tests, executes them in a secure <strong>E2B Sandbox</strong>, and autonomously fixes bugs until the tests pass.</p>
    </div>

    <div class="card">
        <h2>📍 System Architecture</h2>
        <p>The heart of this project is a state machine that handles the logic of code generation and validation.</p>
        
        <div class="img-placeholder" style="margin-bottom: 2rem;">
            [1. Graph Output Image: LangGraph Node Architecture]
        </div>

        <div class="node-list">
            <div class="node-item">
                <div><strong>1. Generate Code:</strong> Translates requirements into Python logic.</div>
            </div>
            <div class="node-item">
                <div><strong>2. Review Code:</strong> Performs a static analysis for best practices.</div>
            </div>
            <div class="node-item">
                <div><strong>3. Generate Tests:</strong> Creates a comprehensive pytest suite.</div>
            </div>
            <div class="node-item">
                <div><strong>4. Run Tests:</strong> Executes code inside an isolated E2B cloud sandbox.</div>
            </div>
            <div class="node-item">
                <div><strong>5. Analyze Failures:</strong> If tests fail, it identifies the root cause and loops back.</div>
            </div>
            <div class="node-item">
                <div><strong>6. Summary:</strong> Provides a formatted final report.</div>
            </div>
        </div>
    </div>

    <div class="card">
        <h2>📸 Project Walkthrough</h2>
        <div class="gallery-grid">
            <div>
                <h3>1. User Interface</h3>
                <div class="img-placeholder">[2. UI Screenshot: Input Requirements]</div>
                <p><small>Streamlit dashboard for real-time interaction.</small></p>
            </div>
            <div>
                <h3>2. Live Execution</h3>
                <div class="img-placeholder">[3. Execution Screenshot: Node Expansion]</div>
                <p><small>Watch the agent's thought process unfold.</small></p>
            </div>
            <div>
                <h3>3. Sandbox Testing</h3>
                <div class="img-placeholder">[4. Testing Screenshot: Pytest Logs]</div>
                <p><small>Isolated code execution via E2B.</small></p>
            </div>
            <div>
                <h3>4. Final Report</h3>
                <div class="img-placeholder">[5. Summary Screenshot: Markdown Output]</div>
                <p><small>The final validated code and review summary.</small></p>
            </div>
        </div>
    </div>

    <div class="card">
        <h2>🚀 Getting Started</h2>
        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.10+</li>
            <li>E2B API Key</li>
            <li>Google AI Studio API Key</li>
        </ul>

        <h3>Installation</h3>
        <pre># Clone the repository
git clone https://github.com/DeepakMishra99/Autonomous-CodeReview-Testing-Agent.git
cd Autonomous-CodeReview-Testing-Agent

# Install dependencies
pip install -r requirements.txt</pre>

        <h3>Environment Setup</h3>
        <pre>export GOOGLE_API_KEY="your-gemini-key"
export E2B_API_KEY="your-e2b-key"</pre>

        <h3>Run</h3>
        <pre>streamlit run app.py</pre>
    </div>

    <div class="card">
        <h2>🛠️ Tech Stack</h2>
        <div class="tech-grid">
            <div class="tech-tag">📦 LangGraph</div>
            <div class="tech-tag">🧠 gemini-3.1-flash-lite-preview</div>
            <div class="tech-tag">🛡️ E2B Sandbox</div>
            <div class="tech-tag">🎨 Streamlit</div>
        </div>
    </div>
</div>

</body>
