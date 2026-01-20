# Implement UNDO & REDO

## Problem Statement
You are given an empty text document.
You must support the following operations:

- append(x): add character x
- undo(): remove last appended character
- redo(): restore last undone character
- read(): return document content

---

## Key Idea

Use **two stacks**:
1. Document stack → current content
2. Redo stack → stores undone characters

---

## Operations Explained

### Append(x)
- Add character to document
- Clear redo stack (new change breaks redo history)

### Undo()
- Remove last character from document
- Push it into redo stack

### Redo()
- Pop from redo stack
- Append back to document

### Read()
- Convert document list to string

---

## Example

Operations:
append(A)
append(B)
append(C)
undo()
read() -> "AB"
redo()
read() -> "ABC"

yaml
Copy code

---

## Time & Space Complexity

- Each operation: `O(1)`
- Read(): `O(n)`
- Space: `O(n)`

---

## Interview Tip
Say:
> "UNDO–REDO is implemented using two stacks.
> One for current state, one for redo history."

---

## Conclusion
This is a classic **stack-based design problem** commonly asked in interviews.
