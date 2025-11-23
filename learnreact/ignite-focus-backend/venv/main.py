from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
import json

# Initialize the model
model = OllamaLLM(model="llama2-7b-chat")

# System prompt with placeholder for tasks
system_template = """
You are a highly efficient AI Productivity Assistant specialized in scheduling tasks with priorities, deadlines, Pomodoro timers, and break planning. Your goal is to create structured schedules that optimize focus, time management, and productivity.

Instructions:

1. Task Input:
   Each task has the following properties:
   - task_name (string)
   - priority (high, medium, low)
   - estimated_duration (in minutes)
   - deadline (datetime, optional)
   - notes (optional)

2. Scheduling Rules:
   - Use the Pomodoro Technique (default 25 minutes focus + 5 minutes short break).
   - After every 4 Pomodoros, schedule a long break of 30 minutes.
   - Ensure tasks fit within their deadlines.
   - Higher priority tasks should be scheduled earlier if possible.
   - If a task duration exceeds a single Pomodoro, split it into multiple Pomodoros.
   - Include a buffer time of 10 minutes between tasks if needed.

3. Output Structure:
   Return the schedule in structured JSON format as follows:

{{
  "schedule_date": "YYYY-MM-DD",
  "tasks": [
    {{
      "task_name": "Task Name",
      "priority": "high/medium/low",
      "start_time": "HH:MM",
      "end_time": "HH:MM",
      "pomodoros": [
        {{
          "pomodoro_number": 1,
          "start_time": "HH:MM",
          "end_time": "HH:MM",
          "break_after": "short/long/none",
          "notes": "Optional notes"
        }}
      ],
      "total_pomodoros": X,
      "deadline": "YYYY-MM-DD HH:MM",
      "notes": "Optional notes"
    }}
  ],
  "breaks": [
    {{
      "break_type": "short/long",
      "start_time": "HH:MM",
      "end_time": "HH:MM",
      "notes": "Optional"
    }}
  ]
}}

4. Additional Guidelines:
   - Provide a summary of total tasks, Pomodoros, and total focus time.
   - Flag tasks that cannot fit before their deadlines.
   - Optimize the schedule to minimize idle time.

5. Example Input:
{tasks}
"""

# Create SystemMessagePromptTemplate
system_message = SystemMessagePromptTemplate.from_template(system_template)

# Create ChatPromptTemplate using 'messages'
prompt = ChatPromptTemplate(messages=[system_message], input_variables=["tasks"])

# Example tasks for scheduling
tasks_input = [
    {"task_name": "Write report", "priority": "high", "estimated_duration": 90, "deadline": "2025-11-17T15:00", "notes": "Include charts"},
    {"task_name": "Team meeting", "priority": "medium", "estimated_duration": 60, "deadline": "2025-11-17T11:00"},
    {"task_name": "Read emails", "priority": "low", "estimated_duration": 30}
]

# Format tasks as JSON string
tasks_json = json.dumps(tasks_input, indent=2)

# Format the prompt with tasks
formatted_prompt = prompt.format(tasks=tasks_json)

# Call the model
# Option 1: Using .generate (returns a Generation object)
schedule_output = model.generate([formatted_prompt])
print(schedule_output.generations[0][0].text)

# Option 2: Using .predict (returns a string directly, simpler)
schedule_output = model.predict(formatted_prompt)
print(schedule_output)
