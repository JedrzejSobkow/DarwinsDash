import uuid


class World:
    
    def __init__(self, seed: int = 42) -> None:
        self.seed: int = seed
        self.entities: set[uuid.UUID] = set()
        self.components_by_type: dict[type, dict[uuid.UUID, Any]] = {}

        
    def create_entity(self) -> uuid.UUID:
        new_entity_id = uuid.uuid4()
        self.entities.add(new_entity_id)
        return new_entity_id
    
    def delete_entity(self, entity_id: uuid.UUID) -> list[Any]:
        self.entities.discard(entity_id)
        
        entity_components: list[Any] = []
        for components_dict in self.components_by_type.values():
            component = components_dict.pop(entity_id, None)
            if component:
                entity_components.append(component)
                
        return entity_components
    
