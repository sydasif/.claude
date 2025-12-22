#!/usr/bin/env bash
set -euo pipefail

GEMINI_BIN="${GEMINI_BIN:-gemini}"
FLAGS="-o text --debug=false"

# Parse arguments
TARGET_PATH=""
ANALYSIS_TYPE="general"

while [[ $# -gt 0 ]]; do
  case $1 in
    --type)
      ANALYSIS_TYPE="$2"
      shift 2
      ;;
    *)
      TARGET_PATH="$1"
      shift
      ;;
  esac
done

if [ -z "$TARGET_PATH" ]; then
  echo "No target path provided"
  echo "Usage: $0 <path_to_code> [--type <analysis_type>]"
  echo "Analysis types: general, security, performance, best-practices, refactoring"
  exit 1
fi

if [ ! -e "$TARGET_PATH" ]; then
  echo "Error: Path '$TARGET_PATH' does not exist"
  exit 1
fi

# Determine if it's a file or directory and read content
if [ -f "$TARGET_PATH" ]; then
  # Single file
  echo "Analyzing file: $TARGET_PATH"
  CODE_CONTENT=$(cat "$TARGET_PATH")
  FILE_TYPE="file"
elif [ -d "$TARGET_PATH" ]; then
  # Directory - get a summary of the directory structure and sample files
  echo "Analyzing directory: $TARGET_PATH"
  DIR_STRUCTURE=$(find "$TARGET_PATH" -type f -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.tsx" -o -name "*.go" -o -name "*.rs" -o -name "*.java" -o -name "*.cpp" -o -name "*.c" -o -name "*.h" -o -name "*.cs" -o -name "*.rb" -o -name "*.php" -o -name "*.html" -o -name "*.css" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.md" | head -20)

  CODE_CONTENT="Directory structure and files:\n\n"
  for file in $DIR_STRUCTURE; do
    if [ -f "$file" ] && [ $(stat -c%s "$file" 2>/dev/null || echo 10000) -lt 50000 ]; then  # Skip files larger than 50KB
      CODE_CONTENT="$CODE_CONTENT\n--- File: $file ---\n"
      CODE_CONTENT="$CODE_CONTENT$(cat "$file" | head -100)\n"  # Limit to first 100 lines of each file
    fi
  done
  FILE_TYPE="directory"
else
  echo "Error: Path '$TARGET_PATH' is neither a file nor a directory"
  exit 1
fi

# Create appropriate prompt based on analysis type
case $ANALYSIS_TYPE in
  "security")
    PROMPT="Act as a security code reviewer. Analyze the following code for potential security vulnerabilities, unsafe practices, and security risks. Provide specific recommendations for improvements.

Target: $TARGET_PATH ($FILE_TYPE)
Code content:
$CODE_CONTENT"
    ;;
  "performance")
    PROMPT="Act as a performance optimization expert. Analyze the following code for performance bottlenecks, inefficiencies, and optimization opportunities. Provide specific recommendations for improvements.

Target: $TARGET_PATH ($FILE_TYPE)
Code content:
$CODE_CONTENT"
    ;;
  "best-practices")
    PROMPT="Act as a code quality expert. Analyze the following code for adherence to best practices, coding standards, and design patterns. Provide specific recommendations for improvements.

Target: $TARGET_PATH ($FILE_TYPE)
Code content:
$CODE_CONTENT"
    ;;
  "refactoring")
    PROMPT="Act as a senior software engineer. Analyze the following code for refactoring opportunities, code smells, and maintainability issues. Provide specific recommendations for improvements.

Target: $TARGET_PATH ($FILE_TYPE)
Code content:
$CODE_CONTENT"
    ;;
  *)
    PROMPT="Act as a senior software engineer and code reviewer. Analyze the following code for quality, structure, potential issues, best practices, and improvement opportunities. Provide a comprehensive analysis with specific recommendations.

Target: $TARGET_PATH ($FILE_TYPE)
Code content:
$CODE_CONTENT"
    ;;
esac

# Run gemini with the prompt and suppress diagnostic output
$GEMINI_BIN $FLAGS "$PROMPT" 2>/dev/null