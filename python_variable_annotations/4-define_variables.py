#!/usr/bin/env python3
"""
This module defines and annotates variables with specific types and values.
"""

a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "ALX"

# function call
if __name__ == "__main__":
    print(f"a is a {type(a)} with a value of {a}")
    print(f"pi is a {type(pi)} with a value of {pi}")
    print(f"i_understand_annotations is a {type(i_understand_annotations)} with a value of {i_understand_annotations}")
    print(f"school is a {type(school)} with a value of {school}")
    
    # Show annotations
    print("\nAnnotations:")
    print(f"a: {a.__annotations__ if hasattr(a, '__annotations__') else 'No annotations on variable'}")