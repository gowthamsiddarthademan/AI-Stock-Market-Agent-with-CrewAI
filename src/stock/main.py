#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from stock.crew import Stock

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
import os

os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    """
    inputs = {
        'sector': 'Any sector of your choice',
    }

    # Create and run the crew
    result = Stock().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)


if __name__ == "__main__":
    run()