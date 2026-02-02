import uuid

from game.core.exceptions import EntityDoesNotExist, ComponentAlreadyExists, ComponentMissing


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
        if entity_id not in self.entities:
            raise EntityDoesNotExist(entity_id, "delete entity")
        self.entities.discard(entity_id)
        
        entity_components: list[Any] = []
        for components_dict in self.components_by_type.values():
            component = components_dict.pop(entity_id, None)
            if component:
                entity_components.append(component)
                
        return entity_components
    
    def add_component(self, entity_id: uuid.UUID, component: Any) -> None:
        if entity_id not in self.entities:
            raise EntityDoesNotExist(entity_id, f"add component {type(component).__name__}")
        
        # TODO Check if such component exists
        
        # Component does not exist yet
        if type(component) not in self.components_by_type:
            self.components_by_type[type(component)] = {entity_id: component}
        # Component for the given entity already exists
        elif entity_id in self.components_by_type[type(component)]:
            raise ComponentAlreadyExists(entity_id, type(component))
        else:
            self.components_by_type[type(component)][entity_id] = component
            
    def remove_component(self, entity_id: uuid.UUID, component_type: type) -> Any:
        if entity_id not in self.entities:
            raise EntityDoesNotExist(entity_id, f"remove component {component_type.__name__}")
        
        # TODO Check if such component exists
        if (component_type not in self.components_by_type or 
            entity_id not in self.components_by_type[component_type]):
             raise ComponentMissing(entity_id, component_type)
        
        
        return self.components_by_type[component_type].pop(entity_id)
    
    def get_component(self, entity_id: uuid.UUID, component_type: type) -> Any:
        if entity_id not in self.entities:
            raise EntityDoesNotExist(entity_id, f"get component {component_type.__name__}")
        
        if (component_type not in self.components_by_type or
            entity_id not in self.components_by_type[component_type]):
            raise ComponentMissing(entity_id, component_type)
        
        return self.components_by_type[component_type][entity_id]
    
    def get_components(self, entity_id: uuid.UUID) -> list[Any]:
        if entity_id not in self.entities:
            raise EntityDoesNotExist(entity_id, f"get components")
        
        components: list[Any] = []
        for entities_components in self.components_by_type.values():
            if entity_id in entities_components:
                components.append(entities_components[entity_id])
                
        return components
    
    def query(self, *component_types: type) -> set[uuid.UUID]:
        if not component_types:
            return set()
        
        if component_types[0] not in self.components_by_type:
            return set()
        entities = set(self.components_by_type[component_types[0]].keys())

        for type in component_types[1:]:
            if type not in self.components_by_type:
                return set()
            entities &= self.components_by_type[type].keys()

        return entities