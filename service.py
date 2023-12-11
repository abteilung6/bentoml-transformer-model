"""
Service encapsulates components likes Runners and API server.

Runner in BentoML is a computational unit that encapsulates
a machine learning model.
"""

import bentoml

# Creates a `summarizer_runner` instance from model.
summarizer_runner = bentoml.models.get("summarization:latest").to_runner()

# Wraps the Runner and creates a Service.
svc = bentoml.Service(
    name="summarization", runners=[summarizer_runner]
)


# Specifies the API endpoint for the Service and
# the logic to process the inputs and outputs
@svc.api(input=bentoml.io.Text(), output=bentoml.io.Text())
async def summarize(text: str) -> str:
    generated = await summarizer_runner.async_run(text, max_length=3000)
    return generated[0]["summary_text"]
