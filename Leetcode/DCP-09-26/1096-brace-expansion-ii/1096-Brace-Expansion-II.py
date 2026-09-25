class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0
        self.expr = expression
        res = self.parse_expr()
        return sorted(list(res))

    def parse_expr(self) -> set:
        """
        Parses an expression: terms separated by commas (Union).
        Expr -> Term (',' Term)*
        """
        res = set()
        while self.i < len(self.expr):
            res.update(self.parse_term())
            if self.i < len(self.expr) and self.expr[self.i] == ',':
                self.i += 1  # Skip ','
            else:
                break
        return res

    def parse_term(self) -> set:
        """
        Parses a term: factors concatenated together (Cartesian Product).
        Term -> Factor+
        """
        res = {""}
        while self.i < len(self.expr) and self.expr[self.i] not in "},":
            factor = self.parse_factor()
            # Compute Cartesian product of current result and new factor
            res = {s1 + s2 for s1 in res for s2 in factor}
        return res

    def parse_factor(self) -> set:
        """
        Parses a factor: either a single letter or a parenthesized Expr {...}.
        Factor -> letter | '{' Expr '}'
        """
        if self.expr[self.i] == '{':
            self.i += 1  # Skip '{'
            res = self.parse_expr()
            self.i += 1  # Skip '}'
            return res
        else:
            char = self.expr[self.i]
            self.i += 1
            return {char}
