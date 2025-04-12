---
title: Hands-On Introduction to the Model Context Protocol (MCP)
date: 2025-04-09
layout: layout/post.html
tags:
  - posts
  - Java
  - AI
  - MCP
  - Python
  
---

For the past few weeks, I’ve been experimenting with Retrieval-Augmented Generation (RAG) to customize and enhance local knowledge-based LLM models. During my research, I came across the **Model Context Protocol (MCP)**, which has been gaining attention for addressing similar challenges that RAG aims to solve. Naturally, I had to try it out.

Currently, there are two official implementations of the MCP protocol (as of now): **Node.js** and **Python**. For my proof of concept (POC), I chose Python due to its flexibility and strong ecosystem for AI development.

**Overall Arch**

<img src="../images/mcp.png" alt="Overall Arch" width="800" height="600">



---

### 1. **Setting Up the Python Environment**

To get started, you’ll need to set up a Python environment with the necessary dependencies for MCP. This includes installing the MCP library and configuring your project for seamless integration.

- Install uv from [Astral](https://github.com/astral-sh/uv)
- Install Python using `uv python install 3.12`

---

### 2. **Creating a Simple FastMCP Application**

In this section, we’ll walk through building a basic FastMCP application. FastMCP is a lightweight framework designed to simplify the implementation of the MCP protocol in Python. In this project we will integrate with local mysql database to display booking data from. 

- `git clone https://github.com/nemo97/sql-mcp.git`
- `uv sync` will download all dependecies and create virtual environment `.venv`
- execute this to enable profile `source .venv/bin/activate`
---

**entry point [Server.py ]**

This is the entry point for mcp server. We will defind all the tools here. You can also defined custom template prompt and other resources, but haven't tried yet.

<img src="../images/server.png" alt="Server.py" width="800" height="500">



**data_reader.py** 
Helps to fetch data from MYSQL database.

<img src="../images/data_reader.png" alt="data_reader.py" width="800" height="500">




### 3. **Configuring MCP with LLM**

Once the FastMCP application is ready, the next step is to integrate it with a local knowledge-based LLM. This involves configuring the MCP protocol to interact with your LLM model, enabling it to process and respond to context-rich queries effectively.

- config in VsCode workspace, you can cofngure as user level or worksoace level (this is very new features,its available in Insider version in Linux) for deatils follow
[VS Code Documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) provides detailed instructions on configuring MCP servers.

When you open `~/workspace/.vscode/mcp.json`, you will find options to start, restart, or stop individual MCP servers.

<img src="../images/mcp_config.png" alt="MCP Client Configuration" width="800" height="500">

Once the server starts successfully, you should see the tools menu in the CoPilot chatbox. Ensure that you are in agent mode for this functionality.

<img src="../images/tools.png" alt="MCP Tools Menu" width="800" height="500">

### Results

Below are sample outputs demonstrating the successful execution of MCP:

<img src="../images/output1.png" alt="Sample Output 1" width="800" height="500">

<img src="../images/output2.png" alt="Sample Output 2" width="800" height="500">

---

### 4. **References**

For more details on MCP and its implementations, check out the official documentation and community resources. These references will help you dive deeper into the protocol and explore advanced use cases.

---

### Conclusion

The Model Context Protocol (MCP) offers a powerful alternative to RAG for enhancing LLM models with local knowledge. By leveraging MCP, you can build scalable and efficient applications that address real-world challenges in AI. However, it is still very early to determine if it will replace RAG. Currently, it provides an option to expand operations to the local machine.

If you're interested in learning more about Java architecture or need help with your next project, feel free to [connect with me](mailto:subhas.sing@gmail.com) or check out my [GitHub repository](https://github.com/nemo97/subhas_dev).