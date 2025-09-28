#!/usr/bin/env python3
"""
JobYaari Chatbot Deployment Script
Automates the complete deployment process
"""

import subprocess
import sys
import os
import time

def print_banner():
    print("=" * 60)
    print("🤖 JOBYAARI AI CHATBOT DEPLOYMENT")
    print("=" * 60)

def run_data_extraction():
    """Run the data extraction process"""
    print("\n📊 STEP 1: Starting Data Extraction...")
    print("-" * 40)
    
    try:
        os.chdir("data_extraction")
        result = subprocess.run([sys.executable, "scraper.py"], 
                              capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✅ Data extraction completed successfully!")
            print(f"Output: {result.stdout[:200]}...")
        else:
            print("❌ Data extraction failed!")
            print(f"Error: {result.stderr}")
            return False
            
        os.chdir("..")
        return True
        
    except subprocess.TimeoutExpired:
        print("⏰ Data extraction timed out!")
        return False
    except Exception as e:
        print(f"❌ Error during data extraction: {e}")
        return False

def check_knowledge_base():
    """Check if knowledge base was created"""
    print("\n🧠 STEP 2: Checking Knowledge Base...")
    print("-" * 40)
    
    kb_path = "chatbot_app/training_data/knowledge_base.json"
    if os.path.exists(kb_path):
        print("✅ Knowledge base found!")
        print(f"Location: {kb_path}")
        return True
    else:
        print("❌ Knowledge base not found!")
        print("Please ensure data extraction completed successfully.")
        return False

def start_chatbot():
    """Start the chatbot application"""
    print("\n🚀 STEP 3: Starting Chatbot Application...")
    print("-" * 40)
    print("📱 Chatbot will be available at: http://localhost:5000")
    print("🔄 Press Ctrl+C to stop the application")
    print("-" * 40)
    
    try:
        os.chdir("chatbot_app")
        subprocess.run([sys.executable, "app.py"])
        
    except KeyboardInterrupt:
        print("\n\n👋 Chatbot application stopped!")
        print("Thank you for using JobYaari AI Chatbot!")
        
    except Exception as e:
        print(f"\n❌ Error starting chatbot: {e}")
        return False
    
    finally:
        os.chdir("..")
    
    return True

def main():
    """Main deployment function"""
    print_banner()
    
    # Check if we're in the right directory
    if not os.path.exists("requirements.txt"):
        print("❌ Please run this script from the project root directory!")
        return
    
    # Step 1: Data Extraction
    if not run_data_extraction():
        print("\n💡 Fix data extraction issues and try again.")
        return
    
    # Step 2: Knowledge Base Check
    if not check_knowledge_base():
        print("\n💡 Knowledge base creation failed. Check data extraction.")
        return
    
    # Step 3: Start Application
    print("\n✅ All checks passed! Starting application...")
    time.sleep(2)
    
    start_chatbot()

if __name__ == "__main__":
    main()
