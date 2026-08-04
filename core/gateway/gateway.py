"""
Main AI Gateway module.
"""
from typing import Dict, Any
from core.gateway.schemas import GatewayResponse
from core.gateway.request_validator import RequestValidator
from core.gateway.response_builder import ResponseBuilder
from core.gateway.exceptions import GatewayValidationError
from core.gateway.middleware import LoggingMiddleware
from utils.logger import get_logger

logger = get_logger("gateway")

class AIGateway:
    """
    The single public entry point to the AI system.
    Handles validation, orchestration delegation, and standardized responses.
    """
    
    def process_request(self, raw_request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes an incoming request through the gateway pipeline.
        Returns a dictionary representation of the standard GatewayResponse.
        """
        # We wrap the internal handler with middleware
        response_obj = LoggingMiddleware.process(raw_request, self._handle_request)
        
        # Convert dataclass to dict for external consumers
        # Doing this manually instead of asdict to handle datetime formatting if needed
        return {
            "status": response_obj.status,
            "request_id": response_obj.request_id,
            "reply": response_obj.reply,
            "actions": response_obj.actions,
            "metadata": response_obj.metadata,
            "usage": response_obj.usage,
            "errors": response_obj.errors
        }

    def _handle_request(self, raw_request: Dict[str, Any]) -> GatewayResponse:
        """Internal handler containing the core pipeline."""
        request_id = raw_request.get("request_id", "unknown")
        
        try:
            # 1. Validate
            validated_request = RequestValidator.validate_and_parse(raw_request)
            
            # 2. Forward to placeholder orchestrator
            orchestrator_reply = self._placeholder_orchestrator(validated_request.message)
            
            # 3. Build success response
            return ResponseBuilder.success(
                request_id=validated_request.request_id,
                reply=orchestrator_reply,
                usage={"tokens": 42} # Placeholder usage
            )
            
        except GatewayValidationError as e:
            logger.error(f"Validation failed for request {request_id}: {e.errors}")
            return ResponseBuilder.error(
                request_id=request_id,
                errors=e.errors
            )
        except Exception as e:
            # Catch all to ensure we don't expose internal stack traces to the client
            logger.error(f"Internal error for request {request_id}: {str(e)}")
            return ResponseBuilder.error(
                request_id=request_id,
                errors=["An internal error occurred while processing the request."]
            )
            
    def _placeholder_orchestrator(self, message: str) -> str:
        """
        Temporary placeholder for the future AI Orchestrator.
        """
        return "AI Gateway connected successfully."
