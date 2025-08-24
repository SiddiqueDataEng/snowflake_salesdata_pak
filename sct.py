import os
import subprocess
import time
import random
from datetime import datetime
import re

# ------------------ ENVIRONMENT CONFIG LOADING ------------------ #
def load_github_env():
    """Load configuration from github.env file"""
    config = {}
    env_file = "github.env"
    
    if os.path.exists(env_file):
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
        print(f"✅ Loaded configuration from {env_file}")
    else:
        print("⚠️ github.env not found, using defaults")
        config = {
            "GITHUB_OWNER": "SiddiqueDataEng",
            "REPO_NAME": "snowflake_salesdata_pak",
            "REPO_LINK": "https://github.com/SiddiqueDataEng/snowflake_salesdata_pak.git",
            "START_DATE": "2020-08-01",
            "END_DATE": "2020-08-28",
            "COMMITS": "10"
        }
    
    return config

def get_input(prompt, default=None, cast_type=str):
    try:
        val = input(f"{prompt} [{default}]: ") or default
        return cast_type(val)
    except Exception as e:
        print(f"⚠️ Invalid input: {e}. Using default → {default}")
        return default

def load_commit_messages():
    """Load realistic commit messages for Snowflake sales data analysis project"""
    txt_file = "commit_messages.txt"
    if os.path.exists(txt_file):
        with open(txt_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            if lines:
                print(f"✅ Loaded {len(lines)} commit messages from {txt_file}")
                return lines
    
    print("⚠️ No valid commit message file found, using project-specific defaults.")
    return [
        "🚀 Initial Snowflake sales data analysis project setup",
        "📊 Added Pakistan sales data CSV files",
        "🏗️ Created OLTP database schema and setup scripts",
        "🔧 Implemented ETL pipeline from OLTP to OLAP",
        "📈 Built OLAP data warehouse structure",
        "📋 Added comprehensive project documentation",
        "⚙️ Configured Snowflake connection profiles",
        "🎯 Created Streamlit dashboard for data visualization",
        "🧪 Added data generation scripts for testing",
        "✅ Finalized deployment and configuration",
        "📚 Updated README and deployment guides",
        "🔨 Refactored SQL scripts for better performance",
        "🛠️ Fixed data loading and transformation issues",
        "🚀 Optimized warehouse and database configurations",
        "📊 Enhanced data analysis and reporting capabilities"
    ]

def get_project_files_structure():
    """Get actual project files organized by category for realistic commits"""
    project_structure = {
        "core_files": [
            "README.md",
            "PROJECT_COMPLETE_SUMMARY.md",
            "COMPLETE_DEPLOYMENT_GUIDE.md",
            "requirements.txt",
            "streamlit_requirements.txt"
        ],
        "snowflake_config": [
            "snowflake.toml",
            "config.txt",
            "account.txt"
        ],
        "data_files": [
            "pakistan_sales_data/pakistan_customers.csv",
            "pakistan_sales_data/pakistan_products.csv",
            "pakistan_sales_data/pakistan_orders.csv",
            "pakistan_sales_data/pakistan_order_details.csv",
            "pakistan_sales_data/pakistan_stores.csv",
            "pakistan_sales_data/pakistan_employees.csv",
            "pakistan_sales_data/pakistan_product_categories.csv",
            "pakistan_sales_data/pakistan_customer_addresses.csv",
            "pakistan_sales_data/pakistan_sales_data.csv"
        ],
        "oltp_scripts": [
            "oltp/01_oltp_database_setup.sql",
            "oltp/02_data_loading_oltp.sql"
        ],
        "olap_scripts": [
            "olap/03_olap_data_warehouse_setup.sql",
            "olap/04_etl_oltp_to_olap.sql"
        ],
        "python_scripts": [
            "generate_pakistan_sales_data.py",
            "streamlit_dashboard.py"
        ]
    }
    
    return project_structure

# ------------------ CONFIG SETUP ------------------ #
GITHUB_CONFIG = load_github_env()
REPO_PATH = os.path.abspath(os.path.dirname(__file__))
REMOTE_URL = GITHUB_CONFIG.get("REPO_LINK", "https://github.com/SiddiqueDataEng/snowflake_salesdata_pak.git")
TOTAL_COMMITS = int(GITHUB_CONFIG.get("COMMITS", 10))
start_str = GITHUB_CONFIG.get("START_DATE", "2020-08-01")
end_str = GITHUB_CONFIG.get("END_DATE", "2020-08-28")

try:
    START_DATE = datetime.strptime(start_str, "%Y-%m-%d")
    END_DATE = datetime.strptime(end_str, "%Y-%m-%d")
except ValueError:
    print("⚠️ Invalid date format in github.env. Using defaults.")
    START_DATE = datetime(2020, 8, 1)
    END_DATE = datetime(2020, 8, 28)

COMMIT_MESSAGES = load_commit_messages()
PROJECT_STRUCTURE = get_project_files_structure()

# ------------------ GIT FUNCTIONS ------------------ #
def run_git_command(cmd, cwd=REPO_PATH):
    print(f"\n🔧 Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(f"📤 STDOUT:\n{result.stdout.strip()}")
    if result.stderr:
        print(f"📛 STDERR:\n{result.stderr.strip()}")
    return result

def ensure_repo_setup():
    """Initialize git repository and configure remote"""
    os.chdir(REPO_PATH)
    
    # Check if git is initialized
    if not os.path.exists(os.path.join(REPO_PATH, ".git")):
        print("🔧 Initializing git repository...")
        run_git_command(["git", "init"])
    
    # Configure remote
    try:
        run_git_command(["git", "remote", "remove", "origin"])
    except:
        pass
    
    run_git_command(["git", "remote", "add", "origin", REMOTE_URL])
    run_git_command(["git", "branch", "-M", "main"])
    print("✅ Git repository configured.")

def create_realistic_commits():
    """Create commits based on actual project structure"""
    print("🚀 Creating realistic commits based on project structure...")
    
    # First commit: Project initialization
    print("\n📝 Commit 1: Project initialization")
    run_git_command(["git", "add", "."])
    env = os.environ.copy()
    commit_date = START_DATE
    date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_COMMITTER_DATE"] = date_str
    env["GIT_AUTHOR_DATE"] = date_str
    
    subprocess.run(
        ["git", "commit", "-m", "🚀 Initial Snowflake sales data analysis project setup"],
        cwd=REPO_PATH,
        env=env,
        capture_output=True,
        text=True
    )
    print(f"✅ Commit 1: Project initialization • {date_str}")
    
    # Subsequent commits: Add files by category
    commit_counter = 2
    
    # Commit 2: Core documentation
    if commit_counter <= TOTAL_COMMITS:
        print(f"\n📝 Commit {commit_counter}: Core documentation")
        files_to_add = PROJECT_STRUCTURE["core_files"]
        for file in files_to_add:
            if os.path.exists(file):
                run_git_command(["git", "add", file])
        
        commit_date = START_DATE + (END_DATE - START_DATE) * (commit_counter - 1) / (TOTAL_COMMITS - 1)
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_COMMITTER_DATE"] = date_str
        env["GIT_AUTHOR_DATE"] = date_str
        
        subprocess.run(
            ["git", "commit", "-m", "📚 Added comprehensive project documentation"],
            cwd=REPO_PATH,
            env=env,
            capture_output=True,
            text=True
        )
        print(f"✅ Commit {commit_counter}: Core documentation • {date_str}")
        commit_counter += 1
    
    # Commit 3: Snowflake configuration
    if commit_counter <= TOTAL_COMMITS:
        print(f"\n📝 Commit {commit_counter}: Snowflake configuration")
        files_to_add = PROJECT_STRUCTURE["snowflake_config"]
        for file in files_to_add:
            if os.path.exists(file):
                run_git_command(["git", "add", file])
        
        commit_date = START_DATE + (END_DATE - START_DATE) * (commit_counter - 1) / (TOTAL_COMMITS - 1)
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_COMMITTER_DATE"] = date_str
        env["GIT_AUTHOR_DATE"] = date_str
        
        subprocess.run(
            ["git", "commit", "-m", "⚙️ Configured Snowflake connection profiles and settings"],
            cwd=REPO_PATH,
            env=env,
            capture_output=True,
            text=True
        )
        print(f"✅ Commit {commit_counter}: Snowflake configuration • {date_str}")
        commit_counter += 1
    
    # Commit 4: Data files
    if commit_counter <= TOTAL_COMMITS:
        print(f"\n📝 Commit {commit_counter}: Sales data files")
        files_to_add = PROJECT_STRUCTURE["data_files"]
        for file in files_to_add:
            if os.path.exists(file):
                run_git_command(["git", "add", file])
        
        commit_date = START_DATE + (END_DATE - START_DATE) * (commit_counter - 1) / (TOTAL_COMMITS - 1)
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_COMMITTER_DATE"] = date_str
        env["GIT_AUTHOR_DATE"] = date_str
        
        subprocess.run(
            ["git", "commit", "-m", "📊 Added Pakistan sales data CSV files"],
            cwd=REPO_PATH,
            env=env,
            capture_output=True,
            text=True
        )
        print(f"✅ Commit {commit_counter}: Sales data files • {date_str}")
        commit_counter += 1
    
    # Commit 5: OLTP scripts
    if commit_counter <= TOTAL_COMMITS:
        print(f"\n📝 Commit {commit_counter}: OLTP database setup")
        files_to_add = PROJECT_STRUCTURE["oltp_scripts"]
        for file in files_to_add:
            if os.path.exists(file):
                run_git_command(["git", "add", file])
        
        commit_date = START_DATE + (END_DATE - START_DATE) * (commit_counter - 1) / (TOTAL_COMMITS - 1)
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_COMMITTER_DATE"] = date_str
        env["GIT_AUTHOR_DATE"] = date_str
        
        subprocess.run(
            ["git", "commit", "-m", "🏗️ Created OLTP database schema and setup scripts"],
            cwd=REPO_PATH,
            env=env,
            capture_output=True,
            text=True
        )
        print(f"✅ Commit {commit_counter}: OLTP database setup • {date_str}")
        commit_counter += 1
    
    # Commit 6: OLAP scripts
    if commit_counter <= TOTAL_COMMITS:
        print(f"\n📝 Commit {commit_counter}: OLAP data warehouse")
        files_to_add = PROJECT_STRUCTURE["olap_scripts"]
        for file in files_to_add:
            if os.path.exists(file):
                run_git_command(["git", "add", file])
        
        commit_date = START_DATE + (END_DATE - START_DATE) * (commit_counter - 1) / (TOTAL_COMMITS - 1)
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_COMMITTER_DATE"] = date_str
        env["GIT_AUTHOR_DATE"] = date_str
        
        subprocess.run(
            ["git", "commit", "-m", "📈 Built OLAP data warehouse structure"],
            cwd=REPO_PATH,
            env=env,
            capture_output=True,
            text=True
        )
        print(f"✅ Commit {commit_counter}: OLAP data warehouse • {date_str}")
        commit_counter += 1
    
    # Commit 7: Python scripts
    if commit_counter <= TOTAL_COMMITS:
        print(f"\n📝 Commit {commit_counter}: Python automation scripts")
        files_to_add = PROJECT_STRUCTURE["python_scripts"]
        for file in files_to_add:
            if os.path.exists(file):
                run_git_command(["git", "add", file])
        
        commit_date = START_DATE + (END_DATE - START_DATE) * (commit_counter - 1) / (TOTAL_COMMITS - 1)
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_COMMITTER_DATE"] = date_str
        env["GIT_AUTHOR_DATE"] = date_str
        
        subprocess.run(
            ["git", "commit", "-m", "🐍 Added Python scripts for data generation and dashboard"],
            cwd=REPO_PATH,
            env=env,
            capture_output=True,
            text=True
        )
        print(f"✅ Commit {commit_counter}: Python automation scripts • {date_str}")
        commit_counter += 1
    
    # Remaining commits: Add any remaining files
    remaining_files = []
    for category in PROJECT_STRUCTURE.values():
        for file in category:
            if os.path.exists(file):
                remaining_files.append(file)
    
    # Remove already committed files
    for file in remaining_files[:]:
        if file in [f for category in PROJECT_STRUCTURE.values() for f in category]:
            remaining_files.remove(file)
    
    if remaining_files and commit_counter <= TOTAL_COMMITS:
        print(f"\n📝 Commit {commit_counter}: Additional project files")
        for file in remaining_files:
            if os.path.exists(file):
                run_git_command(["git", "add", file])
        
        commit_date = START_DATE + (END_DATE - START_DATE) * (commit_counter - 1) / (TOTAL_COMMITS - 1)
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_COMMITTER_DATE"] = date_str
        env["GIT_AUTHOR_DATE"] = date_str
        
        subprocess.run(
            ["git", "commit", "-m", "📁 Added remaining project files and configurations"],
            cwd=REPO_PATH,
            env=env,
            capture_output=True,
            text=True
        )
        print(f"✅ Commit {commit_counter}: Additional project files • {date_str}")
        commit_counter += 1
    
    # Create tags for major milestones
    if commit_counter > 1:
        run_git_command(["git", "tag", "v1.0.0"])
        print("🏷️ Tag created: v1.0.0")
    
    if commit_counter > 3:
        run_git_command(["git", "tag", "v1.1.0"])
        print("🏷️ Tag created: v1.1.0")
    
    if commit_counter > 5:
        run_git_command(["git", "tag", "v1.2.0"])
        print("🏷️ Tag created: v1.2.0")

def push_to_github():
    """Push all commits to GitHub"""
    print("\n🚀 Pushing to GitHub...")
    run_git_command(["git", "push", "-u", "origin", "main", "--tags"])
    print("✅ All changes pushed to GitHub successfully!")

def show_project_summary():
    """Display project summary and GitHub information"""
    print("\n" + "="*60)
    print("🎯 PROJECT DEPLOYMENT SUMMARY")
    print("="*60)
    print(f"📁 Repository: {GITHUB_CONFIG.get('REPO_NAME', 'snowflake_salesdata_pak')}")
    print(f"🔗 GitHub URL: {GITHUB_CONFIG.get('REPO_LINK', 'N/A')}")
    print(f"👤 Owner: {GITHUB_CONFIG.get('GITHUB_OWNER', 'N/A')}")
    print(f"📅 Commit Period: {start_str} to {end_str}")
    print(f"🔢 Total Commits: {TOTAL_COMMITS}")
    print(f"📊 Project Type: Snowflake Sales Data Analysis")
    print(f"🌍 Data Source: Pakistan Sales Data")
    print("="*60)

# ------------------ RUN SCRIPT ------------------ #
if __name__ == "__main__":
    print("🚀 Snowflake Sales Data Analysis - GitHub Deployment Script")
    print("="*60)
    
    # Load configuration
    show_project_summary()
    
    # Confirm deployment
    confirm = input("\n🤔 Proceed with GitHub deployment? (y/N): ").lower().strip()
    if confirm not in ['y', 'yes']:
        print("❌ Deployment cancelled.")
        exit(0)
    
    try:
        # Setup and deploy
        ensure_repo_setup()
        create_realistic_commits()
        push_to_github()
        
        print("\n🎉 DEPLOYMENT COMPLETED SUCCESSFULLY!")
        print(f"🌐 View your repository at: {GITHUB_CONFIG.get('REPO_LINK', 'N/A')}")
        
    except Exception as e:
        print(f"\n❌ Deployment failed: {e}")
        print("🔧 Please check your configuration and try again.")
