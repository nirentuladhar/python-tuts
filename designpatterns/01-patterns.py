types of design patterns

- creational
    uses polymorphism
    used to create objects in a systematic way
    flexible. different subtypes of objects from the same class can be created at runtime
- structural
    uses inheritance
    establishes useful relationships between software components in certain configurations
    accomplish both functional and nonfunctional goals
    different goals yield different structures
- behavioural
    uses methods and their signatures
    best practices of objects interaction
    define the protocols

classes are templates to create objects
to avoid recreating them each time.
eg. cookie cutter: replicate objects

classes define objects in terms of:
    - attributes
        represents properties of an entity
        captures the state of the entity
    - methods
        represents behaviours




inheritance:
    establishes a relationship between two classes as parent and child.

    child class:
        keeps the attributes & methods of its parent
        adds new attributes or methods of its own
        can override existing methods of parent


polymorphism:
    relies on inheritance
    allows child classes to be instantiated and treated as the same type as its parent
    enables a parent class to be manifested into any of its child classes
    true nature of the object is hidden until runtime or until one of the methods is invoked.


pattern language

- name
    should capture the gist of the problem
    becomes part of a vocabulary during the design process
    needs to be meaningful and memorable
- context
    provides a scenario
    provides more insights
        when to or when not to use
- problem
    describes the design challenge
- solution
    specifies a pattern
        structure: relationships among elements
        behaviour: interactions
- related patterns
    lists other patterns
        used together with the pattern being described
        similar but different



    