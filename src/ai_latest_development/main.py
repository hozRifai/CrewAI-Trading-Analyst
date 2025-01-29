#!/usr/bin/env python
import sys
import warnings

from crew import AiLatestDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    inputs = {
        'topic': 'Stocks Trading Algorithms'
    }
    AiLatestDevelopment().crew().kickoff(inputs=inputs)

run()