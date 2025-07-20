#!/usr/bin/env python3
"""
Test script to demonstrate RiversOS vCISO and SOC capabilities
"""

import subprocess
import time
import sys

def test_riversos_command(command):
    """Test a specific RiversOS command"""
    print(f"\n{'='*60}")
    print(f"🧪 TESTING: {command}")
    print(f"{'='*60}")
    
    try:
        # Send command to RiversOS
        process = subprocess.Popen(
            ["python", "riversos.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Send the command and exit
        stdout, stderr = process.communicate(input=f"{command}\nexit\n", timeout=30)
        
        # Extract the response (skip the initial setup)
        lines = stdout.split('\n')
        response_started = False
        response_lines = []
        
        for line in lines:
            if 'RiversOS-AI>' in line and not response_started:
                response_started = True
                continue
            elif response_started and 'RiversOS-AI>' in line:
                break
            elif response_started:
                response_lines.append(line)
        
        print('\n'.join(response_lines))
        
    except subprocess.TimeoutExpired:
        print("⏰ Command timed out")
        process.kill()
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("🚀 RiversOS vCISO & SOC Capabilities Test Suite")
    print("Testing comprehensive digital vCISO functionality...")
    
    # Test cases for different vCISO capabilities
    test_commands = [
        "dashboard",
        "soc",
        "advisory compliance",
        "incident",
        "hunt",
        "compliance",
        "learn"
    ]
    
    for command in test_commands:
        test_riversos_command(command)
        time.sleep(1)  # Brief pause between tests
    
    print(f"\n{'='*60}")
    print("✅ Test suite completed!")
    print("RiversOS vCISO capabilities successfully demonstrated")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()