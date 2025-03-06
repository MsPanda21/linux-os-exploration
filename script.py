# Linux OS Exploration: System Information Script
import os
import platform
import subprocess

def get_system_info():
    """Fetch basic system information"""
    print("🌟 Linux OS System Information 🌟")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Kernel Version: {platform.version()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Machine: {platform.machine()}")
    print(f"CPU: {platform.processor()}")

def list_files():
    """List files in the current directory using Linux command"""
    print("\n📂 Listing files in the current directory:")
    subprocess.run(["ls", "-lh"])  # Runs 'ls -lh' command

def check_disk_usage():
    """Check disk space usage"""
    print("\n💾 Disk Space Usage:")
    subprocess.run(["df", "-h"])  # Runs 'df -h' command

# Execute functions
get_system_info()
list_files()
check_disk_usage()
