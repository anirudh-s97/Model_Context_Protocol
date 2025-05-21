# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
from pywinauto.application import Application
import win32gui
import win32con
import time
import os
from win32api import GetSystemMetrics
import pyautogui

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# Global variables for Paint
paint_app = None

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# PAINT RELATED FUNCTIONS - Updated from draw_paint_v2.py

@mcp.tool()
async def open_paint() -> dict:
    """Instantiates Microsoft Paint in a clean state and return.
    """
    global paint_app
    try:
        # Close any existing Paint instances
        os.system("taskkill /f /im mspaint.exe 2>nul")
        time.sleep(1)
        
        # Start Paint
        paint_app = Application(backend="uia").start('mspaint.exe')
        time.sleep(2)
        
        # Get the Paint window
        paint_window = paint_app.window(title_re=".*Paint.*")
        
        # Maximize it
        paint_window.maximize()
        time.sleep(1)
        
        return "Paint application is started and is active now" #{
        #     "content": [
        #         TextContent(
        #             type="text",
        #             text="Paint application is initialized"
        #         )
        #     ]
        # }
    except Exception as e:
        return f"Error opening Paint: {str(e)}" #{
        #     "content": [
        #         TextContent(
        #             type="text",
        #             text=
        #         )
        #     ]
        # }

@mcp.tool()
async def draw_outline_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Draw an unfilled rectangular border on the current Paint canvas.

    Parameters
    ----------
    x1, y1 : int
        Screen coordinates (in pixels) of the **top‑left** corner of the rectangle.
    x2, y2 : int
        Screen coordinates (in pixels) of the **bottom‑right** corner of the          rectangle.
    """

    def select_rectangle_tool() -> dict:
        """Select the rectangle shape tool"""
        try:
            # Press Escape to cancel any current operations
            pyautogui.press('esc')
            time.sleep(0.5)
            
            # Access Home tab and shapes
            pyautogui.hotkey('alt', 'h')
            time.sleep(0.5)
            pyautogui.press('sh')  # Shapes button
            time.sleep(0.5)
            
            # Click on rectangle (first shape in the menu)
            screen_width, screen_height = pyautogui.size()
            shape_x = int(screen_width * 0.25)
            shape_y = 155
            pyautogui.click(shape_x, shape_y)
            time.sleep(0.5)
            
            # Select outline style (no fill)
            pyautogui.hotkey('alt', 'h')
            time.sleep(0.3)
            pyautogui.press('so')  # Shape outline
            time.sleep(0.5)
            
            return "Rectangle tool selected"

        except Exception as e:
            return f"Error selecting rectangle tool: {str(e)}"



    try:
        # Ensure rectangle tool is selected
        select_rectangle_tool()
        time.sleep(0.5)
        
        # Draw the rectangle by dragging from (x1,y1) to (x2,y2)
        pyautogui.moveTo(x1, y1)
        time.sleep(0.3)
        pyautogui.dragTo(x2, y2, duration=0.8)
        time.sleep(1)
        
        return f"Rectangle drawn from ({x1},{y1}) to ({x2},{y2})"

    except Exception as e:
        return f"Error drawing rectangle: {str(e)}"
    

@mcp.tool()
async def add_text_to_paint(text: str) -> dict:
    """Insert text at the centre of the current Paint canvas.


    Parameters
    ----------
    text : str
        The string to display inside the newly created text box.  New‑line       characters (``\n``) are honoured by Paint.

    """
    try:
        # Cancel any current tool selection
        pyautogui.press('esc')
        time.sleep(0.5)
        
        # Select text tool
        pyautogui.hotkey('alt', 'h')
        time.sleep(0.3)
        pyautogui.press('t')
        time.sleep(1)
        
        # Get screen center for text placement
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width // 2
        center_y = screen_height // 2
        
        # Create text area inside the rectangle
        text_x1 = center_x - 250  # Smaller than rectangle
        text_y1 = center_y - 50
        text_x2 = center_x + 250
        text_y2 = center_y + 50
        
        # Click and drag to create text box
        pyautogui.moveTo(text_x1, text_y1)
        time.sleep(0.3)
        pyautogui.dragTo(text_x2, text_y2, duration=0.5)
        time.sleep(1)
        
        # Format text - center align and increase size
        pyautogui.hotkey('ctrl', 'e')  # Center align
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'shift', '>')  # Increase font size
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'shift', '>')  # Increase again
        time.sleep(0.3)
        
        # Type the provided text
        pyautogui.write(text)
        time.sleep(0.5)
        
        # Click outside to finish text editing
        pyautogui.click(center_x, center_y + 150)
        time.sleep(0.5)
        
        return f"Text '{text}' added inside rectangle"

    except Exception as e:
        return f"Error adding text: {str(e)}"

# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution