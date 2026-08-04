"""
Base interfaces that future modules can extend.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict

class IModel(ABC):
    """Base interface for all AI models."""
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> Any:
        """Generate a response based on a prompt."""
        pass

class ITool(ABC):
    """Base interface for all agent tools."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Name of the tool."""
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        """Description of what the tool does."""
        pass
        
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Execute the tool's action."""
        pass

class IMemory(ABC):
    """Base interface for agent memory."""
    
    @abstractmethod
    def add_message(self, role: str, content: str) -> None:
        """Add a message to the memory."""
        pass
        
    @abstractmethod
    def get_context(self) -> list:
        """Retrieve the current memory context."""
        pass
        
    @abstractmethod
    def clear(self) -> None:
        """Clear the memory."""
        pass
