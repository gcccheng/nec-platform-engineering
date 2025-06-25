# --- Imports ---
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from validate_peptide import is_valid_peptide  # Logic module
from prometheus_fastapi_instrumentator import Instrumentator

# --- FastAPI app initialization ---
app = FastAPI()

# --- Configure logging ---
logging.basicConfig(
    level=logging.INFO,  # Log level: INFO and above
    format="%(asctime)s %(levelname)s: %(message)s"  # Timestamp + level + message
)
logger = logging.getLogger(__name__)

# --- Define input model using Pydantic ---
class Peptide(BaseModel):
    sequence: str  # The input JSON must contain a string field called "sequence"

# --- Attach Prometheus instrumentation ---
instrumentator = Instrumentator()              # Create a Prometheus middleware
instrumentator.instrument(app).expose(app)     # Instrument all endpoints and expose /metrics

# --- Define the validation endpoint ---
@app.post("/validate")
def validate(peptide: Peptide):
    # Log the incoming request
    logger.info(f"Received sequence: {peptide.sequence}")

    # Validate the sequence
    if is_valid_peptide(peptide.sequence):
        logger.info("Validation passed.")
        return {"valid": True}  # HTTP 200 with JSON response
    else:
        logger.warning("Validation failed.")
        raise HTTPException(status_code=400, detail="Invalid peptide sequence")

