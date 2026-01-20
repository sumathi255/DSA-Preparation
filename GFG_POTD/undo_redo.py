class Solution:
    def __init__(self):
        # Document content as list (easy append/pop)
        self.doc = []
        # Stack to store undone characters for redo
        self.redo_stack = []

    def append(self, x):
        # Append character to document
        self.doc.append(x)
        # Once new append happens, redo history is cleared
        self.redo_stack.clear()

    def undo(self):
        # Undo last append if possible
        if self.doc:
            ch = self.doc.pop()
            self.redo_stack.append(ch)

    def redo(self):
        # Redo last undone operation if possible
        if self.redo_stack:
            ch = self.redo_stack.pop()
            self.doc.append(ch)

    def read(self):
        # Return current document as string
        return "".join(self.doc)
