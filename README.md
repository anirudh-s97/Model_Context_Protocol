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

### Paint Coordinates
Text box positioning can be adjusted in the `add_text_to_paint` function:
```python
# Rectangle coordinates (customizable)
x1, y1 = 780, 380   # Top-left corner
x2, y2 = 1140, 700  # Bottom-right corner
```

## ▶️ Run log (`mcp_client.py`)

<details>
$ ucp run mcp_client.py 
<summary>Starting main execution...
Establishing connection to MCP server...
Connection established, creating session...
Session created, initializing...
Requesting tool list...
Successfully retrieved 22 tools
Creating system prompt...
Number of tools: 22
Added description for tool: 1. add(a: integer, b: integer) - Add two numbers
Added description for tool: 2. add_list(l: array) - Add all numbers in a list
Added description for tool: 3. subtract(a: integer, b: integer) - Subtract two numbers
Added description for tool: 4. multiply(a: integer, b: integer) - Multiply two numbers
Added description for tool: 5. divide(a: integer, b: integer) - Divide two numbers
Added description for tool: 6. power(a: integer, b: integer) - Power of two numbers
Added description for tool: 7. sqrt(a: integer) - Square root of a number
Added description for tool: 8. cbrt(a: integer) - Cube root of a number
Added description for tool: 9. factorial(a: integer) - factorial of a number
Added description for tool: 10. log(a: integer) - log of a number
Added description for tool: 11. remainder(a: integer, b: integer) - remainder of two numbers divison
Added description for tool: 12. sin(a: integer) - sin of a number
Added description for tool: 13. cos(a: integer) - cos of a number
Added description for tool: 14. tan(a: integer) - tan of a number
Added description for tool: 15. mine(a: integer, b: integer) - special mining tool
Added description for tool: 16. create_thumbnail(image_path: string) - Create a thumbnail from an image
Added description for tool: 17. strings_to_chars_to_int(string: string) - Return the ASCII values of the characters in a word
Added description for tool: 18. int_list_to_exponential_sum(int_list: array) - Return sum of exponentials of numbers in a list
Added description for tool: 19. fibonacci_numbers(n: integer) - Return the first n Fibonacci Numbers
Added description for tool: 20. open_paint() - Instantiates Microsoft Paint in a clean state and return.

Added description for tool: 21. draw_outline_rectangle(x1: integer, y1: integer, x2: integer, y2: integer) - Draw an unfilled rectangular border on the current Paint canvas.

    Parameters
    ----------
    x1, y1 : int
        Screen coordinates (in pixels) of the **top‑left** corner of the rectangle.
    x2, y2 : int
        Screen coordinates (in pixels) of the **bottom‑right** corner of the          rectangle.

Added description for tool: 22. add_text_to_paint(text: string) - Insert text at the centre of the current Paint canvas.


    Parameters
    ----------
    text : str
        The string to display inside the newly created text box.  New‑line       characters (``
``) are honoured by Paint.


Successfully created tools description
Created system prompt...
You are a math agent solving problems in iterations. You have access to various mathematical tools.

Available tools:
1. add(a: integer, b: integer) - Add two numbers
2. add_list(l: array) - Add all numbers in a list
3. subtract(a: integer, b: integer) - Subtract two numbers
4. multiply(a: integer, b: integer) - Multiply two numbers
5. divide(a: integer, b: integer) - Divide two numbers
6. power(a: integer, b: integer) - Power of two numbers
7. sqrt(a: integer) - Square root of a number
8. cbrt(a: integer) - Cube root of a number
9. factorial(a: integer) - factorial of a number
10. log(a: integer) - log of a number
11. remainder(a: integer, b: integer) - remainder of two numbers divison
12. sin(a: integer) - sin of a number
13. cos(a: integer) - cos of a number
14. tan(a: integer) - tan of a number
15. mine(a: integer, b: integer) - special mining tool
16. create_thumbnail(image_path: string) - Create a thumbnail from an image
17. strings_to_chars_to_int(string: string) - Return the ASCII values of the characters in a word
18. int_list_to_exponential_sum(int_list: array) - Return sum of exponentials of numbers in a list
19. fibonacci_numbers(n: integer) - Return the first n Fibonacci Numbers
20. open_paint() - Instantiates Microsoft Paint in a clean state and return.

21. draw_outline_rectangle(x1: integer, y1: integer, x2: integer, y2: integer) - Draw an unfilled rectangular border on the current Paint canvas.

    Parameters
    ----------
    x1, y1 : int
        Screen coordinates (in pixels) of the **top‑left** corner of the rectangle.
    x2, y2 : int
        Screen coordinates (in pixels) of the **bottom‑right** corner of the          rectangle.

22. add_text_to_paint(text: string) - Insert text at the centre of the current Paint canvas.


    Parameters
    ----------
    text : str
        The string to display inside the newly created text box.  New‑line       characters (``
``) are honoured by Paint.



You must respond with EXACTLY ONE line in one of these formats (no additional text):
1. For function calls:
   FUNCTION_CALL: function_name|param1|param2|...

Examples:
- FUNCTION_CALL: add|5|3
- FUNCTION_CALL: strings_to_chars_to_int|INDIA

IMPORTANT:

1. COMPLETE ALL CALCULATIONS FIRST: Process every function call and handle all returned values before proceeding to visualization. Never skip computational steps.
2. NO REDUNDANT CALLS: Never repeat identical function calls with the same parameters.

DO NOT include any explanations or additional text.
Your entire response should be a single line starting with FUNCTION_CALL:

Starting iteration loop...

--- Iteration 1 ---
Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
LLM Response: FUNCTION_CALL: strings_to_chars_to_int|INDIA

DEBUG: Raw function info:  strings_to_chars_to_int|INDIA
DEBUG: Split parts: ['strings_to_chars_to_int', 'INDIA']
DEBUG: Function name: strings_to_chars_to_int
DEBUG: Raw parameters: ['INDIA']
DEBUG: Found tool: strings_to_chars_to_int
DEBUG: Tool schema: {'properties': {'string': {'title': 'String', 'type': 'string'}}, 'required': ['string'], 'title': 'strings_to_chars_to_intArguments', 'type': 'object'}
DEBUG: Schema properties: {'string': {'title': 'String', 'type': 'string'}}
DEBUG: Converting parameter string with value INDIA to type string
DEBUG: Final arguments: {'string': 'INDIA'}
DEBUG: Calling tool strings_to_chars_to_int
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='73', annotations=None), TextContent(type='text', text='78', annotations=None), TextContent(type='text', text='68', annotations=None), TextContent(type='text', text='73', annotations=None), TextContent(type='text', text='65', annotations=None)] isError=False
DEBUG: Result has content attribute
73
DEBUG: Final iteration result: ['73', '78', '68', '73', '65']
result_str: [73, 78, 68, 73, 65]

--- Iteration 2 ---
Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
LLM Response: FUNCTION_CALL: int_list_to_exponential_sum|[73, 78, 68, 73, 65]

DEBUG: Raw function info:  int_list_to_exponential_sum|[73, 78, 68, 73, 65]
DEBUG: Split parts: ['int_list_to_exponential_sum', '[73, 78, 68, 73, 65]']
DEBUG: Function name: int_list_to_exponential_sum
DEBUG: Raw parameters: ['[73, 78, 68, 73, 65]']
DEBUG: Found tool: int_list_to_exponential_sum
DEBUG: Tool schema: {'properties': {'int_list': {'items': {}, 'title': 'Int List', 'type': 'array'}}, 'required': ['int_list'], 'title': 'int_list_to_exponential_sumArguments', 'type': 'object'}
DEBUG: Schema properties: {'int_list': {'items': {}, 'title': 'Int List', 'type': 'array'}}
DEBUG: Converting parameter int_list with value [73, 78, 68, 73, 65] to type array
DEBUG: Final arguments: {'int_list': [73, 78, 68, 73, 65]}
DEBUG: Calling tool int_list_to_exponential_sum
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='7.59982224609308e33', annotations=None)] isError=False
DEBUG: Result has content attribute
7.59982224609308e33
DEBUG: Final iteration result: ['7.59982224609308e33']
result_str: [7.59982224609308e33]

--- Iteration 3 ---
Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
LLM Response: FUNCTION_CALL: open_paint

DEBUG: Raw function info:  open_paint
DEBUG: Split parts: ['open_paint']
DEBUG: Function name: open_paint
DEBUG: Raw parameters: []
DEBUG: Found tool: open_paint
DEBUG: Tool schema: {'properties': {}, 'title': 'open_paintArguments', 'type': 'object'}
DEBUG: Schema properties: {}
DEBUG: Final arguments: {}
DEBUG: Calling tool open_paint
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='Paint application is started and is active now', annotations=None)] isError=False
DEBUG: Result has content attribute
Paint application is started and is active now
DEBUG: Final iteration result: ['Paint application is started and is active now']
result_str: [Paint application is started and is active now]

--- Iteration 4 ---
Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
LLM Response: FUNCTION_CALL: add_text_to_paint|7.59982224609308e33

DEBUG: Raw function info:  add_text_to_paint|7.59982224609308e33
DEBUG: Split parts: ['add_text_to_paint', '7.59982224609308e33']
DEBUG: Function name: add_text_to_paint
DEBUG: Raw parameters: ['7.59982224609308e33']
DEBUG: Found tool: add_text_to_paint
DEBUG: Tool schema: {'properties': {'text': {'title': 'Text', 'type': 'string'}}, 'required': ['text'], 'title': 'add_text_to_paintArguments', 'type': 'object'}  
DEBUG: Schema properties: {'text': {'title': 'Text', 'type': 'string'}}
DEBUG: Converting parameter text with value 7.59982224609308e33 to type string
DEBUG: Final arguments: {'text': '7.59982224609308e33'}
DEBUG: Calling tool add_text_to_paint
DEBUG: Raw result: meta=None content=[TextContent(type='text', text="Text '7.59982224609308e33' added inside rectangle", annotations=None)] isError=False
DEBUG: Result has content attribute
Text '7.59982224609308e33' added inside rectangle
DEBUG: Final iteration result: ["Text '7.59982224609308e33' added inside rectangle"]
result_str: [Text '7.59982224609308e33' added inside rectangle]

--- Iteration 5 ---
Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
LLM Response: FUNCTION_CALL: draw_outline_rectangle|100|100|400|300

DEBUG: Raw function info:  draw_outline_rectangle|100|100|400|300
DEBUG: Split parts: ['draw_outline_rectangle', '100', '100', '400', '300']
DEBUG: Function name: draw_outline_rectangle
DEBUG: Raw parameters: ['100', '100', '400', '300']
DEBUG: Found tool: draw_outline_rectangle
DEBUG: Tool schema: {'properties': {'x1': {'title': 'X1', 'type': 'integer'}, 'y1': {'title': 'Y1', 'type': 'integer'}, 'x2': {'title': 'X2', 'type': 'integer'}, 'y2': {'title': 'Y2', 'type': 'integer'}}, 'required': ['x1', 'y1', 'x2', 'y2'], 'title': 'draw_outline_rectangleArguments', 'type': 'object'}
DEBUG: Schema properties: {'x1': {'title': 'X1', 'type': 'integer'}, 'y1': {'title': 'Y1', 'type': 'integer'}, 'x2': {'title': 'X2', 'type': 'integer'}, 'y2': {'title': 'Y2', 'type': 'integer'}}
DEBUG: Converting parameter x1 with value 100 to type integer
DEBUG: Converting parameter y1 with value 100 to type integer
DEBUG: Converting parameter x2 with value 400 to type integer
DEBUG: Converting parameter y2 with value 300 to type integer
DEBUG: Final arguments: {'x1': 100, 'y1': 100, 'x2': 400, 'y2': 300}
DEBUG: Calling tool draw_outline_rectangle
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='Rectangle drawn from (100,100) to (400,300)', annotations=None)] isError=False
DEBUG: Result has content attribute
Rectangle drawn from (100,100) to (400,300)
DEBUG: Final iteration result: ['Rectangle drawn from (100,100) to (400,300)']
result_str: [Rectangle drawn from (100,100) to (400,300)]</summary>

### Screenshot
![image](https://github.com/user-attachments/assets/f59abb0f-0092-48ef-ae6e-b1f1b9f375b7)


### Demo Video
[Watch the demo video](https://youtu.be/L30M8-HMA60)


### Debug Mode
Uncomment the `pdb.set_trace()` line in `mcp_client.py` for step-by-step debugging.
