from calculator import Calculator, LOADED_AT

def test_module_loaded_at():
    # Edit calculator.py and save — watch the timestamp below update instantly
    LOADED_AT  #?

def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    # Try adding a log point or value peek on the line below
    result = calc.add(100, 200)  #?
    assert result == 300

def test_multiply():
    calc = Calculator()
    # Let's fix the error, try clicking Debug code lens on the test
    assert calc.multiply(2, 2) == 5

def test_multiply_negative():
    calc = Calculator()
    # Uncomment the assertion below to cover the other branch in multiply()
    # assert calc.multiply(-1, 3) == 0

"""
Here are some cool things you can quickly try:
  - Time Travel Debugger:  click the Debug code lens above any test
  - Value Peek:            place #? at the end of any expression
  - Logpoints:             use the gutter context menu to log any expression
  - Test Story Viewer:     run 'Open Test Story' to see the full execution flow
  - AI Integration:        use Wallaby's Copilot Chat or MCP Server to debug with AI
"""
