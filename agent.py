# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
import json
import sys
from typing import Any, Optional



def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }



def before_agent_callback(callback_context: Any) -> Optional[Any]:
    """
    Agent lifecycle callback running at the start of every turn.

    - get the user information 
    """

    agent_name = callback_context.agent_name
    print(f"[Callback] Before model call for agent: {agent_name}")
    user_id = callback_context.session.user_id
    print(f"Agent invoked by User ID: {user_id}")
    user_language = extract_browser_language(callback_context)

    # This will generate a clean, searchable jsonPayload
    log_entry = {
        "event": "agent_invocation",
        "user_id": user_id,
        "agent_name": agent_name,
        "message": f"Agent invoked by User ID: {user_id}",
        "user_language": user_language
    }
    print(json.dumps(log_entry), file=sys.stdout)

    

    return None

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-3.8-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather],
    before_agent_callback=[before_agent_callback],
)