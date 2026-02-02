import uuid

class DarwinDashError(Exception):
    """Base class for all exceptions in Darwin's Dash."""
    pass

class EntityDoesNotExist(DarwinDashError):
    """Raised when an action is attempted on an entity ID that is no longer in the World."""
    def __init__(self, entity_id: uuid.UUID, context: str = "execute action"):
        self.entity_id = entity_id
        self.context = context
        self.message = f"Action failed: Entity with UUID {entity_id} does not exist (Context: {context})."
        super().__init__(self.message)
        
class ComponentAlreadyExists(DarwinDashError):
    """Raised when attempting to add a component to an entity that already has one of that type."""
    def __init__(self, entity_id: uuid.UUID, component_type: type):
        self.entity_id = entity_id
        self.component_type = component_type
        self.message = f"Action failed: Entity with UUID {entity_id} already has a component of type: {component_type.__name__}"
        super().__init__(self.message)
        
class ComponentMissing(DarwinDashError):
    """Raised when an entity is expected to have a component but doesn't."""
    def __init__(self, entity_id: uuid.UUID, component_type: type):
        self.entity_id = entity_id
        self.component_type = component_type
        self.message = f"Action failed: Entity with UUID {entity_id} is missing required component: {component_type.__name__}"