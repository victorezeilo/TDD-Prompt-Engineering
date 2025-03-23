"""
Experiment Logger

This module provides logging functionality to track participant activities
during the experiment, including:
- Test runs and results
- File modifications
- Code coverage metrics
- Constraint assignments
"""

import os
import time
import json
import datetime
import coverage

class ExperimentLogger:
    
    def __init__(self, log_file="experiment_log.json"):
        self.log_file = log_file
        self.start_time = time.time()
        
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump({
                    "experiment_start": datetime.datetime.now().isoformat(),
                    "test_runs": [],
                    "file_changes": [],
                    "coverage_reports": [],
                    "task_times": []
                }, f, indent=2)
    
    def log_test_run(self, test_results):
        with open(self.log_file, 'r') as f:
            log_data = json.load(f)
        
        log_data["test_runs"].append({
            "timestamp": datetime.datetime.now().isoformat(),
            "results": test_results
        })
        
        with open(self.log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
    
    def log_file_change(self, filename, action="modified"):
        with open(self.log_file, 'r') as f:
            log_data = json.load(f)
        
        log_data["file_changes"].append({
            "timestamp": datetime.datetime.now().isoformat(),
            "filename": filename,
            "action": action
        })
        
        with open(self.log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
    
    def log_coverage(self):
        cov = coverage.Coverage()
        cov.start()
        
        import unittest
        from test import ItineraryBuilderTest
        
        suite = unittest.TestLoader().loadTestsFromTestCase(ItineraryBuilderTest)
        unittest.TextTestRunner(verbosity=0).run(suite)
        
        cov.stop()
        cov.save()
        
        coverage_data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "total_coverage": cov.report(show_missing=False),
            "file_coverage": {}
        }
        
        for file in cov.get_data().measured_files():
            if os.path.basename(file) in ['main.py', 'test.py']:
                file_cov = cov.analysis(file)
                coverage_data["file_coverage"][os.path.basename(file)] = {
                    "lines_total": len(file_cov[1]),
                    "lines_covered": len(file_cov[2]),
                    "lines_missed": len(file_cov[3]),
                    "percentage": 100 * len(file_cov[2]) / len(file_cov[1]) if len(file_cov[1]) > 0 else 0
                }
        
        with open(self.log_file, 'r') as f:
            log_data = json.load(f)
        
        log_data["coverage_reports"].append(coverage_data)
        
        with open(self.log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        return coverage_data
    
    def log_task_time(self, task_name, duration):
        with open(self.log_file, 'r') as f:
            log_data = json.load(f)
        
        if "task_times" not in log_data:
            log_data["task_times"] = []
        
        log_data["task_times"].append({
            "timestamp": datetime.datetime.now().isoformat(),
            "task": task_name,
            "duration": duration
        })
        
        with open(self.log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
    
    def log_constraints(self, manual_constraints, ai_constraints):
        with open(self.log_file, 'r') as f:
            log_data = json.load(f)
        
        log_data["constraints"] = {
            "manual": manual_constraints,
            "ai": ai_constraints,
            "assigned_at": datetime.datetime.now().isoformat()
        }
        
        with open(self.log_file, 'w') as f:
            json.dump(log_data, f, indent=2)


def run_tests_with_logging():
    logger = ExperimentLogger()
    
    import unittest
    from test import ItineraryBuilderTest
    from io import StringIO
    import sys
    
    output = StringIO()
    runner = unittest.TextTestRunner(stream=output, verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(ItineraryBuilderTest)
    result = runner.run(suite)
    
    test_results = {
        "total": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "skipped": len(result.skipped),
        "success": result.wasSuccessful(),
        "details": output.getvalue()
    }
    
    logger.log_test_run(test_results)
    
    coverage_data = logger.log_coverage()
    
    return test_results, coverage_data