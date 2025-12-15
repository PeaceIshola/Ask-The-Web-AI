"""
Schema generation utilities for tool calling
"""
import inspect


def to_schema(fn):
    """Convert a function to a JSON schema for tool calling.
    
    Args:
        fn: The function to convert
    
    Returns:
        A dictionary describing the tool (its name, args, and types)
    """
    # Get function signature
    sig = inspect.signature(fn)
    
    # Build the schema dictionary
    schema = {
        "name": fn.__name__,
        "description": fn.__doc__.strip() if fn.__doc__ else "",
        "parameters": {}
    }
    
    # Process each parameter
    for param_name, param in sig.parameters.items():
        param_info = {}
        
        # Get type annotation
        if param.annotation != inspect.Parameter.empty:
            param_info["type"] = param.annotation.__name__
        else:
            param_info["type"] = "any"
        
        # Check if parameter has a default value
        if param.default != inspect.Parameter.empty:
            param_info["default"] = param.default
            param_info["required"] = False
        else:
            param_info["required"] = True
        
        schema["parameters"][param_name] = param_info
    
    return schema
