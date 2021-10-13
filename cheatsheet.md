# Python to C# Cheat Sheet

## Comments

C#:

```csharp
// Comment line

/*
  Comment
  block
*/
```

Python:

```python
# Comment
```

## Output

C#:

```csharp
Console.WriteLine("Hello World!");
Console.Write("Hello World!");
```

Python:

```python
print("Hello World!")
```

## Input

C#:

```csharp
Console.ReadLine();
```

Python:

```python
input()
```

## Variables

C#:

```csharp
type variableName = value;
```

Python:

```python
variableName = value
```

## Operators

### Arithmetic Operators

C#:

- `+` Addition (also used for String concatenation)
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulus
- `++` Increment
- `--` Decrement

Python:

- `+` Addition (also used for String concatenation)
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulus
- `**` Exponentiation
- `//` Floor division

### Assignment Operators

C#:

- `Arithmetic Operator/Comparison Operator=` * assignment

Python:

- `Arithmetic operator=` * assignment

### Comparison Operators

C#:

- `==` Equal to
- `!=` Not equal
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

Python:

- `==` Equal to
- `!=` Not equal
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

### Logical Operators

C#:

- `&&` Logical and
- `||` Logical or
- `!` Logical not

Python:

- `and` Returns True if both statements are true
- `or` Returns True if one of the statements is true
- `not` Reverse the result, returns False if the result is true

## Making Decisions

C#:

```csharp
if (condition_1)
{
  // Code
}
else if(condition_2)
{
  // Code
}
else
{
  // Code
}

switch (variable) {
  case integral_literal_1:
    // Code
    break;
  case integral_literal_2:
    // Code
    break;
  case integral_literal_3:
    // Code
    break;
  default:
    // Code
    break;
}
```

Python:

```python
if condition_1:
  # Code
elif condition_2:
  # Code
else:
  # Code
```

## Iterating

C#:

```csharp
for (initialization; condition; increment)
{
  // Code
}

while (condition)
{
  // Code
}

do
{
  // Code
} while (condition);

foreach (var <name_of_local_variable> in <name_of_iterable>)
{
  // Code
}
```

Python:

```python
for varName in range(start,end,stepsize):
  # Codeblock

while <condition>:
  # Code Statements
```

## Data structures consisting of a collection of elements

C# (Arrays):

```csharp
<type>[] <variable_name> = new <type>[<size>];

<type>[] <variable_name> = {
  <comma_separated_list_of_values>
};
```

Python (Lists):

```python
<variable_name> = [<comma_separated_list_of_values>]
```

## Classes

C#:

```csharp
public class <NameOfClass>
{
  // Constructor
  public <NameOfClass>(<arguments>)
  {
    // Code
  }
  
  // Default Constructor
  public <NameOfClass>()
  {
    // Code
  }

  // Methods ...
  <access_modifier> <return_type> NameOfMethod(<arguments>)
  {
    // Code
    return value;
  }

  public override string ToString()
  {
    return "Some String representation of your object";
  }

  // Attributes of the class
  <access_modifier> <data_type> attributeName = <init_value>; // Access modifier for attributes is advised to be private
}
```

Python:

```python
class <NameOfClass>:
  """Descriptive string of class function"""

  # Constructor
  def __init__(self, <arguments>):
    # Initialize object

  # Methods ...
  def <name_of_method>(self, <arguments>):
    # Statements ...
    self.__<name_of_attribute> = <value>

  def __repr__(self):
    return <some_value>
```
