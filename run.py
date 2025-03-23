"""
Experiment Runner

This script provides a interfact to run the tests and manage the experiment
"""

import os
import sys
import time
import textwrap
import random
import json
from logger import run_tests_with_logging, ExperimentLogger

ALL_CONSTRAINTS = [
    "The itinerary should return a list of concerts that state the artist, date, and location of each concert.",
    "The itinerary should return a list of concerts sorted in chronological order (by date from earliest to latest).",
    "An artist has at most one concert in the itinerary. If an artist has more than one concert in the list, the itinerary should only include the one with the earliest start date.",
    "Some artists may have no concerts on the list. In that case, that should be indicated in the itinerary.",
    "No two concerts may take place on the same day. If two different artists (or the same artist) have a concert on the same day, the itinerary only includes the concert closest to the last one.",
    "If an artist only has one concert, it should be prioritized over artists with multiple concerts, regardless if the location is closer or not."
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 80)
    print("         CONCERT ITINERARY BUILDER - TEST-DRIVEN DEVELOPMENT EXPERIMENT")
    print("=" * 80)
    print()

def print_menu():
    print("MENU:")
    print("1. Run tests and view results")
    print("2. View current code coverage")
    print("3. View experiment progress")
    print("4. Record time for a task")
    print("5. View system requirements")
    print("6. Exit")
    print()

def assign_constraints():
    # Användaren får random valda constraints
    indices = list(range(len(ALL_CONSTRAINTS)))
    random.shuffle(indices)
    
    manual_constraints = indices[:3]
    ai_constraints = indices[3:]
    
    return (manual_constraints, ai_constraints)

def save_constraint_assignments(manual_indices, ai_indices):
    log_file = "experiment_log.json"
    
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            log_data = json.load(f)
    else:
        log_data = {
            "experiment_start": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "test_runs": [],
            "file_changes": [],
            "coverage_reports": [],
            "task_times": []
        }
    
    log_data["constraint_assignments"] = {
        "manual": manual_indices,
        "ai_assisted": ai_indices,
        "assigned_at": time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    
    with open(log_file, "w") as f:
        json.dump(log_data, f, indent=2)

def get_constraint_assignments():
    log_file = "experiment_log.json"
    
    if not os.path.exists(log_file):
        return (None, None)
    
    try:
        with open(log_file, "r") as f:
            log_data = json.load(f)
        
        if "constraint_assignments" in log_data:
            manual_indices = log_data["constraint_assignments"]["manual"]
            ai_indices = log_data["constraint_assignments"]["ai_assisted"]
            return (manual_indices, ai_indices)
    except (json.JSONDecodeError, KeyError):
        pass
    
    return (None, None)

def display_tdd_info():
    print("\nTEST-DRIVEN DEVELOPMENT (TDD) OVERVIEW")
    print("-" * 80)
    print("This experiment uses Test-Driven Development (TDD), a software development approach where you:")
    print("1. RED PHASE: Write a failing test that defines a desired function or improvement")
    print("2. GREEN PHASE: Write the simplest code to make the test pass")
    print("3. REFACTOR PHASE: Clean up the code while ensuring tests still pass")
    print()
    print("This 'Red-Green-Refactor' cycle is repeated for each feature or requirement.")
    print("The key principle is to write tests before writing implementation code.")
    print("During this experiment, you'll go through this cycle both manually and with")
    print("AI assistance to explore how these approaches differ.")
    print()

def display_experiment_instructions():
    print("\nEXPERIMENT INSTRUCTIONS")
    print("-" * 80)
    print("You will complete the following steps:")
    print()
    print("PART 1: MANUAL TDD CYCLE")
    print("  1. RED PHASE:")
    print("     - Write three test cases for your manual constraints")
    print("     - Run tests to confirm they fail")
    print("     - Record time spent")
    print()
    print("  2. GREEN PHASE:")
    print("     - Implement code to make your manual tests pass")
    print("     - Run tests to confirm they pass")
    print("     - Record time spent")
    print()
    print("  3. REFACTOR PHASE:")
    print("     - Improve your implementation while keeping tests passing")
    print("     - Record time spent")
    print()
    print("PART 2: AI-ASSISTED TDD CYCLE")
    print("  1. RED PHASE:")
    print("     - Use AI to help write three test cases for your AI-assigned constraints")
    print("     - Run tests to confirm they fail")
    print("     - Record time spent")
    print()
    print("  2. GREEN PHASE:")
    print("     - Extend implementation to make AI-assisted tests pass")
    print("     - Run tests to confirm they pass")
    print("     - Record time spent")
    print()
    print("  3. REFACTOR PHASE:")
    print("     - Improve your implementation while keeping tests passing")
    print("     - Record time spent")
    print()

def display_assigned_constraints(manual_indices, ai_indices):
    print("\nYOUR ASSIGNED CONSTRAINTS")
    print("-" * 80)
    print("\nFor MANUAL test writing (implement these first):")
    for i, idx in enumerate(manual_indices, 1):
        print(f"  {i}. {ALL_CONSTRAINTS[idx]}")
    
    print("\nFor AI-ASSISTED test writing (implement these second):")
    for i, idx in enumerate(ai_indices, 1):
        print(f"  {i}. {ALL_CONSTRAINTS[idx]}")
    
    print("\nRemember: Follow the TDD cycle (Red-Green-Refactor) for each set of constraints.")
    print()

def run_tests():
    print("Running tests...")
    print()
    
    start_time = time.time()
    test_results, coverage_data = run_tests_with_logging()
    elapsed_time = time.time() - start_time
    
    print(f"Tests completed in {elapsed_time:.2f} seconds.")
    print(f"Total tests run: {test_results['total']}")
    print(f"Passed: {test_results['total'] - test_results['failures'] - test_results['errors']}")
    print(f"Failed: {test_results['failures']}")
    print(f"Errors: {test_results['errors']}")
    print()
    
    if test_results['failures'] > 0 or test_results['errors'] > 0:
        print("Test Output:")
        print("-" * 80)
        print(textwrap.indent(test_results['details'], '  '))
        print("-" * 80)
    else:
        print("All tests passed!")
    
    print()
    print(f"Overall code coverage: {coverage_data['total_coverage']:.2f}%")
    for file, metrics in coverage_data['file_coverage'].items():
        print(f"  {file}: {metrics['percentage']:.2f}% ({metrics['lines_covered']}/{metrics['lines_total']} lines)")
    
    input("\nPress Enter to continue...")

def view_coverage():
    print("Generating coverage report...")
    
    import coverage
    cov = coverage.Coverage()
    cov.start()
    
    import unittest
    from test import ItineraryBuilderTest
    
    suite = unittest.TestLoader().loadTestsFromTestCase(ItineraryBuilderTest)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    cov.stop()
    
    print("\nCODE COVERAGE REPORT:")
    print("-" * 80)
    cov.report()
    print("-" * 80)
    
    input("\nPress Enter to continue...")

def view_progress():
    import json
    
    try:
        with open("experiment_log.json", "r") as f:
            log_data = json.load(f)
        
        print("\nEXPERIMENT PROGRESS:")
        print("-" * 80)
        print(f"Experiment started: {log_data.get('experiment_start', 'N/A')}")
        print(f"Total test runs: {len(log_data.get('test_runs', []))}")
        print(f"Total file changes: {len(log_data.get('file_changes', []))}")
        
        if log_data.get('test_runs'):
            latest_run = log_data['test_runs'][-1]
            print("\nLatest test run:")
            print(f"  Time: {latest_run['timestamp']}")
            print(f"  Tests passed: {latest_run['results']['total'] - latest_run['results']['failures'] - latest_run['results']['errors']} / {latest_run['results']['total']}")
        
        if log_data.get('coverage_reports'):
            latest_cov = log_data['coverage_reports'][-1]
            print("\nLatest coverage report:")
            print(f"  Time: {latest_cov['timestamp']}")
            print(f"  Overall coverage: {latest_cov.get('total_coverage', 0):.2f}%")
            
            for file, metrics in latest_cov.get('file_coverage', {}).items():
                print(f"  {file}: {metrics['percentage']:.2f}% ({metrics['lines_covered']}/{metrics['lines_total']} lines)")
        
        if log_data.get('task_times'):
            print("\nRecorded task times:")
            for task in log_data.get('task_times', []):
                print(f"  {task['task']}: {task['duration']} minutes")
        
    except (FileNotFoundError, json.JSONDecodeError):
        print("No experiment progress data available yet.")
    
    input("\nPress Enter to continue...")

def record_time():
    print("\nRECORD TASK TIME:")
    print("-" * 80)
    print("Tasks:")
    print("1. Manual test writing (RED phase)")
    print("2. Manual implementation (GREEN phase)")
    print("3. Manual refactoring (REFACTOR phase)")
    print("4. AI-assisted test writing (RED phase)")
    print("5. AI-assisted implementation (GREEN phase)")
    print("6. AI-assisted refactoring (REFACTOR phase)")
    print("7. Other (specify)")
    
    try:
        task_type = int(input("\nSelect task type (1-7): "))
        if task_type < 1 or task_type > 7:
            raise ValueError("Invalid selection")
        
        if task_type == 7:
            task_name = input("Enter task name: ")
        else:
            task_names = [
                "Manual test writing (RED phase)",
                "Manual implementation (GREEN phase)",
                "Manual refactoring (REFACTOR phase)",
                "AI-assisted test writing (RED phase)",
                "AI-assisted implementation (GREEN phase)",
                "AI-assisted refactoring (REFACTOR phase)"
            ]
            task_name = task_names[task_type - 1]
        
        duration = float(input("Enter time spent (in minutes): "))
        
        logger = ExperimentLogger()
        logger.log_task_time(task_name, duration)
        
        print(f"\nRecorded {duration} minutes for '{task_name}'.")
        
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
    
    input("\nPress Enter to continue...")

def view_requirements():
    manual_indices, ai_indices = get_constraint_assignments()
    
    print("\nCONCERT ITINERARY BUILDER - SYSTEM REQUIREMENTS")
    print("-" * 80)
    print("User Story:")
    print("  As a user, I want to build an itinerary of upcoming concerts of my favorite")
    print("  artists so that I can attend the concerts.")
    print()
    print("All Constraints:")
    for i, constraint in enumerate(ALL_CONSTRAINTS, 1):
        print(f"  {i}. {constraint}")
    
    if manual_indices and ai_indices:
        print("\nYOUR ASSIGNED CONSTRAINTS:")
        print("\nFor MANUAL test writing:")
        for i, idx in enumerate(manual_indices, 1):
            print(f"  {i}. {ALL_CONSTRAINTS[idx]}")
        
        print("\nFor AI-ASSISTED test writing:")
        for i, idx in enumerate(ai_indices, 1):
            print(f"  {i}. {ALL_CONSTRAINTS[idx]}")
    
    print("\nTest-Driven Development Process:")
    print("  1. RED: Write a failing test")
    print("  2. GREEN: Write code to make the test pass")
    print("  3. REFACTOR: Improve your code while keeping tests passing")
    
    input("\nPress Enter to continue...")

def main():
    """Main program loop."""
    manual_indices, ai_indices = get_constraint_assignments()
    
    if manual_indices is None or ai_indices is None:
        clear_screen()
        print_header()
        
        display_tdd_info()
        input("\nPress Enter to continue...")
        
        manual_indices, ai_indices = assign_constraints()
        save_constraint_assignments(manual_indices, ai_indices)
        
        clear_screen()
        print_header()
        display_experiment_instructions()
        input("\nPress Enter to continue...")
        
        clear_screen()
        print_header()
        display_assigned_constraints(manual_indices, ai_indices)
        input("\nPress Enter to continue to the main menu...")
    
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        choice = input("Select an option (1-6): ")
        print()
        
        if choice == "1":
            run_tests()
        elif choice == "2":
            view_coverage()
        elif choice == "3":
            view_progress()
        elif choice == "4":
            record_time()
        elif choice == "5":
            view_requirements()
        elif choice == "6":
            print("Exiting the experiment runner. Thank you for participating!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    random.seed(42)
    main()