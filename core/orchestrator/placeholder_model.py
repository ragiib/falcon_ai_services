"""
Temporary model service to verify the orchestration pipeline.
"""
from core.orchestrator.schemas import OrchestratorContext
from utils.logger import get_logger

logger = get_logger("orchestrator.placeholder_model")

class PlaceholderModel:
    """A deterministic model replacement for testing the pipeline."""
    
    @staticmethod
    def execute(context: OrchestratorContext) -> OrchestratorContext:
        """Simulates processing a request based on intent."""
        logger.info(f"Executing placeholder model for intent: {context.intent}")
        
        # Echo the message with the intent
        reply = f"[{context.intent.upper()}] Request successfully processed by the Orchestrator. You said: '{context.request.message}'"
        
        context.model_response = reply
        context.usage = {"tokens": len(context.request.message.split())}
        
        return context
