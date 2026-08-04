"""
Routes requests to the appropriate component based on intent.
"""
from core.orchestrator.schemas import OrchestratorContext
from core.orchestrator.placeholder_model import PlaceholderModel
from utils.logger import get_logger

logger = get_logger("orchestrator.dispatcher")

class Dispatcher:
    """Selects the next processing component."""
    
    @staticmethod
    def dispatch(context: OrchestratorContext) -> OrchestratorContext:
        """Routes to the model (currently always the placeholder)."""
        logger.info(f"Dispatching request {context.request.request_id} with intent '{context.intent}'")
        
        # In the future, logic here will route to specific models or agents
        # based on context.intent. For now, always use PlaceholderModel.
        return PlaceholderModel.execute(context)
