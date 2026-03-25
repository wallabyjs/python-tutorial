# Wallaby.py Python Tutorial

A sample Python project for exploring [Wallaby.py](https://wallabypy.com) features.

## Getting Started

1. Open this project in VS Code with the Wallaby.py extension installed
2. Wallaby.py will start automatically
3. Open `test_calculator.py` to see real-time test feedback

## What to Try

- **Real-time test execution**: Open `test_calculator.py` and notice the `LOADED_AT` timestamp shown inline next to `LOADED_AT  #?` in `test_module_loaded_at`. Make any edit to `calculator.py` (e.g. add a space or change a comment) and save — the timestamp updates instantly, showing the exact time the module was reloaded.
- **Fix a bug**: The multiply test in `test_calculator.py` has an intentional error in `test_multiply`. Fix the assertion and watch the test pass/fail indicators update in real-time.
- **Code coverage**: Uncomment tests in `test_car.py` to see coverage change in real-time
- **Value Peek**: Add `#?` at the end of any expression to inspect its value
- **Logpoints**: Right-click the gutter to add a logpoint and inspect values without modifying code
- **Time Travel Debugger**: Click the `Debug` code lens above any test to step forward and backward through execution
- **Test Story Viewer**: Run the `Open Test Story` command within any test to see the full execution flow in a single view
- **Interactive Value Graphs**: Log a complex object (e.g. `#?` on a DeLorean instance) within `test_delorean.py`, and click the graph icon to visualize it
- **AI Integration**: Use Wallaby's Copilot Chat integration (`Investigate with AI`) from the Errors list to debug with AI

## Project Structure

- `calculator.py` / `test_calculator.py` - Basic arithmetic with a bug to fix, value peek demo
- `car.py` / `test_car.py` - Code coverage exploration with `print()` output
- `delorean.py` / `test_delorean.py` - Time Travel Debugger and value graph demo
