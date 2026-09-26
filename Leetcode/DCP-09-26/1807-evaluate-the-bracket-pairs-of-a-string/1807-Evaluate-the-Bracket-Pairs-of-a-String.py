class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Build a lookup hash map from the knowledge list
        d = dict(knowledge)
        
        res = []
        in_bracket = False
        current_key = []
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key = "".join(current_key)
                res.append(d.get(key, "?"))
                current_key = []
            elif in_bracket:
                current_key.append(char)
            else:
                res.append(char)
                
        return "".join(res)