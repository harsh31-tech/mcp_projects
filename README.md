# MCP Project

A hands-on learning repository for exploring the **Model Context Protocol (MCP)** in Python — built while learning core concepts and applying them to small, practical projects.

## About

This repo documents my journey into MCP, covering the core prerequisites and building progressively toward real server/client implementations. It also serves as a practice ground before applying MCP concepts to larger projects like **ServerFlow** (a Visual Backend Builder).

## Goals

- Understand MCP architecture: Client ↔ Server ↔ LLM communication
- Get comfortable with Python prerequisites needed for MCP: `async/await`, decorators, and `Pydantic`
- Build small MCP servers and clients to internalize the protocol
- Document learnings, mistakes, and fixes along the way

## Roadmap

- [ ] **Phase 1** – Python prerequisites (async/await, decorators, Pydantic basics)
- [ ] **Phase 2** – MCP fundamentals (Client SDK, Server SDK, tool/resource definitions)
- [ ] **Phase 3** – Building a basic MCP server (custom tools)
- [ ] **Phase 4** – Connecting MCP server to an LLM client
- [ ] **Phase 5** – Mini-projects using MCP end-to-end

## Tech Stack

- **Language:** Python
- **Core Concepts:** async/await, decorators, Pydantic
- **Protocol:** Model Context Protocol (MCP)

## Project Structure

```
mcp_project/
├── phase1_basics/        # Python prerequisite practice
├── phase2_mcp_intro/      # MCP fundamentals
├── phase3_servers/        # Custom MCP server implementations
├── phase4_client_llm/     # MCP client + LLM integration
├── phase5_projects/       # Mini practice projects
└── README.md
```

## Setup

```bash
git clone https://github.com/<your-username>/mcp_project.git
cd mcp_project
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Progress Log

I'll be documenting key learnings and updates as I go — feel free to follow along or reach out if you're learning MCP too!

## Connect

If you're also learning MCP or building with it, let's connect and share notes.

---
*This repo is a work in progress and will evolve as I move through each phase.*