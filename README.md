# MCP Calculator Agent with Paint Integration

A Python-based Model Context Protocol (MCP) implementation that creates an intelligent mathematical agent capable of performing calculations and visualizing results in Microsoft Paint.

## What is Model Context Protocol (MCP)?

Model Context Protocol (MCP) is an open protocol that enables AI assistants to securely connect to external data sources and tools. It provides a standardized way for AI models to interact with various resources, databases, and applications while maintaining security and control.

Key benefits of MCP:
- **Standardized Integration**: Uniform way to connect AI models with external tools
- **Security**: Controlled access to resources with proper authentication
- **Extensibility**: Easy addition of new tools and capabilities
- **Interoperability**: Works across different AI platforms and applications

## Project Overview

This project demonstrates MCP in action by creating a mathematical agent that can:

1. **Perform Complex Calculations**: Access to 20+ mathematical functions
2. **Process String Data**: Convert strings to ASCII values and perform operations
3. **Visual Output**: Display results in Microsoft Paint with text boxes and shapes
4. **Iterative Problem Solving**: Multi-step approach to complex mathematical problems

## Architecture

### Components

**MCP Server (`mcp_server.py`)**
- Implements FastMCP server with mathematical tools
- Provides 20+ calculation functions (basic arithmetic, trigonometry, special operations)
- Includes Microsoft Paint automation tools
- Handles string processing and list operations

**MCP Client (`mcp_client.py`)**
- Connects to the MCP server using stdio transport
- Integrates with Google's Gemini 2.0 Flash model for AI reasoning
- Implements iterative problem-solving with timeout protection
- Manages conversation state and tool execution flow

## Available Tools

### Mathematical Operations
- **Basic Arithmetic**: `add`, `subtract`, `multiply`, `divide`
- **Advanced Math**: `power`, `sqrt`, `cbrt`, `factorial`, `log`
- **Trigonometry**: `sin`, `cos`, `tan`
- **List Operations**: `add_list`, `fibonacci_numbers`
- **String Processing**: `strings_to_chars_to_int`
- **Exponential**: `int_list_to_exponential_sum`
- **Custom**: `mine` (special mining operation), `remainder`

### Paint Integration Tools
- **`open_paint()`**: Launch and initialize Microsoft Paint
- **`draw_outline_rectangle(x1, y1, x2, y2)`**: Draw rectangular borders
- **`add_text_to_paint(text)`**: Insert formatted text with automatic centering

## Installation & Setup

### Prerequisites
```bash
# Required Python packages
pip install python-dotenv
pip install mcp
pip install google-genai
pip install pywinauto
pip install pyautogui
pip install pillow
pip install pywin32
```

### Environment Configuration
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

### System Requirements
- **Operating System**: Windows (required for Paint integration)
- **Python**: 3.8 or higher
- **Microsoft Paint**: Pre-installed Windows application

## Usage

### Running the Agent
```bash
python mcp_client.py
```

### Example Problem
The default query demonstrates the agent's capabilities:
```
"Find the ASCII values of characters in INDIA and then compute the sum of exponentials of those values. Wrap the final resultant value inside a text box from the Paint Application"
```

This query showcases:
1. String to ASCII conversion: `INDIA` → `[73, 78, 68, 73, 65]`
2. Exponential calculation: `e^73 + e^78 + e^68 + e^73 + e^65`
3. Visual output in Microsoft Paint

### Execution Flow
1. **Tool Discovery**: Client requests available tools from server
2. **AI Planning**: Gemini model analyzes the problem and selects appropriate tools
3. **Iterative Execution**: Up to 5 iterations of tool calls with results
4. **Visualization**: Final result displayed in Paint with formatted text box

## Technical Features

### Safety & Reliability
- **Timeout Protection**: 10-second timeout for AI generation to prevent hanging
- **Error Handling**: Comprehensive exception handling throughout the pipeline
- **State Management**: Global state reset between executions
- **Input Validation**: Type checking and parameter validation for all tools

### AI Integration
- **Model**: Google Gemini 2.0 Flash for intelligent tool selection
- **Prompt Engineering**: Structured system prompts for consistent tool usage
- **Function Mapping**: Automatic parameter parsing and type conversion
- **Result Processing**: Intelligent handling of various return types

### Windows Automation
- **PyAutoGUI**: Screen automation for Paint interaction
- **PyWinAuto**: Windows application control and management
- **Win32API**: System-level operations and window management

## Configuration

### Iteration Control
```python
max_iterations = 5  # Maximum number of problem-solving iterations
```

### Timeout Settings
```python
timeout = 10  # Seconds for AI generation timeout
```

## 📋 Execution Log

Below is the execution log of the math agent processing a task:

<details open>
<summary><b>🔄 Process Initialization</b></summary>

```
Starting main execution...
Establishing connection to MCP server...
Connection established, creating session...
Session created, initializing...
Requesting tool list...
Successfully retrieved 22 tools
Creating system prompt...
```
</details>

<details open>
<summary><b>🛠️ Available Tools</b></summary>

The math agent has access to 22 tools:

1. `add(a: integer, b: integer)` - Add two numbers
2. `add_list(l: array)` - Add all numbers in a list
3. `subtract(a: integer, b: integer)` - Subtract two numbers
4. `multiply(a: integer, b: integer)` - Multiply two numbers
5. `divide(a: integer, b: integer)` - Divide two numbers
6. `power(a: integer, b: integer)` - Power of two numbers
7. `sqrt(a: integer)` - Square root of a number
8. `cbrt(a: integer)` - Cube root of a number
9. `factorial(a: integer)` - factorial of a number
10. `log(a: integer)` - log of a number
11. `remainder(a: integer, b: integer)` - remainder of two numbers divison
12. `sin(a: integer)` - sin of a number
13. `cos(a: integer)` - cos of a number
14. `tan(a: integer)` - tan of a number
15. `mine(a: integer, b: integer)` - special mining tool
16. `create_thumbnail(image_path: string)` - Create a thumbnail from an image
17. `strings_to_chars_to_int(string: string)` - Return the ASCII values of the characters in a word
18. `int_list_to_exponential_sum(int_list: array)` - Return sum of exponentials of numbers in a list
19. `fibonacci_numbers(n: integer)` - Return the first n Fibonacci Numbers
20. `open_paint()` - Instantiates Microsoft Paint in a clean state
21. `draw_outline_rectangle(x1: integer, y1: integer, x2: integer, y2: integer)` - Draw an unfilled rectangular border
22. `add_text_to_paint(text: string)` - Insert text at the centre of the Paint canvas
</details>

<details open>
<summary><b>🔄 Execution Flow</b></summary>

### Iteration 1: Convert String to ASCII Values
```
FUNCTION_CALL: strings_to_chars_to_int|INDIA
Result: [73, 78, 68, 73, 65]
```

### Iteration 2: Calculate Exponential Sum
```
FUNCTION_CALL: int_list_to_exponential_sum|[73, 78, 68, 73, 65]
Result: 7.59982224609308e33
```

### Iteration 3: Initialize Paint
```
FUNCTION_CALL: open_paint
Result: Paint application is started and is active now
```

### Iteration 4: Add Text to Paint
```
FUNCTION_CALL: add_text_to_paint|7.59982224609308e33
Result: Text '7.59982224609308e33' added inside rectangle
```

### Iteration 5: Draw Outline Rectangle
```
FUNCTION_CALL: draw_outline_rectangle|100|100|400|300
Result: Rectangle drawn from (100,100) to (400,300)
```
</details>


### Screenshot
![image](https://github.com/user-attachments/assets/f59abb0f-0092-48ef-ae6e-b1f1b9f375b7)


### Demo Video
[Watch the demo video](https://youtu.be/L30M8-HMA60)


### Debug Mode
Uncomment the `pdb.set_trace()` line in `mcp_client.py` for step-by-step debugging.
