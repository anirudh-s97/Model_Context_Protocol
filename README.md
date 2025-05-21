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

## Example Output

For the default query about "INDIA":
1. **ASCII Conversion**: `[73, 78, 68, 73, 65]`
2. **Exponential Sum**: `4.758...e+33` (approximate)
3. **Paint Visualization**: Text box with the final result displayed

## Limitations

- **Windows Only**: Paint integration requires Windows operating system
- **Paint Dependency**: Requires Microsoft Paint to be available
- **Screen Resolution**: Paint automation may need adjustment for different screen sizes
- **API Costs**: Uses Google Gemini API which may incur costs

## Contributing

This project demonstrates MCP capabilities and can be extended with:
- Additional mathematical functions
- More visualization tools
- Cross-platform support
- Advanced error recovery
- Custom tool categories

## License

This project serves as an educational example of MCP implementation. Please ensure you comply with the terms of service for all integrated APIs and tools.

## Troubleshooting

### Common Issues
1. **Paint Not Opening**: Ensure Windows Paint is installed and accessible
2. **API Errors**: Verify Gemini API key is correctly set in `.env`
3. **Tool Execution Failures**: Check Python package installations
4. **Screen Automation Issues**: Adjust coordinates for your screen resolution

### Debug Mode
Uncomment the `pdb.set_trace()` line in `mcp_client.py` for step-by-step debugging.