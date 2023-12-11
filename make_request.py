import requests

SAMPLE_TEXT = "Change my mind"

response = requests.post(
   "http://0.0.0.0:3000/summarize",
   headers={
      "accept": "text/plain",
      "Content-Type": "text/plain",
   },
   data=SAMPLE_TEXT,
)

print(f"[RESPONSE] {response.text}")
