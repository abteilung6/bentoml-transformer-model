"""Download a model to the local Model Store

Usage: `python download_model.py``
Manage model with `bentoml models list`
"""

from typing import Final
import transformers
import bentoml

MODEL_CNN: Final[str] = "sshleifer/distilbart-cnn-12-6"
TASK_SUM: Final[str] = "summarization"

bentoml.transformers.save_model(
    TASK_SUM,
    transformers.pipeline(TASK_SUM, model=MODEL_CNN),
    metadata=dict(model_name=MODEL_CNN),
)
