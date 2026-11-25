class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        remove_left = 0
        remove_right = 0

        for ch in s:
            if ch == "(":
                remove_left += 1
            elif ch == ")":
                if remove_left > 0:
                    remove_left -= 1
                else:
                    remove_right += 1

        res: list[str] = []
        seen: set[str] = set()

        def dfs(
            idx: int,
            balance: int,
            rem_l: int,
            rem_r: int,
            path: list[str],
        ) -> None:
            if balance < 0 or rem_l < 0 or rem_r < 0:
                return

            if idx == len(s):
                if balance == 0 and rem_l == 0 and rem_r == 0:
                    candidate = "".join(path)
                    if candidate not in seen:
                        seen.add(candidate)
                        res.append(candidate)
                return

            ch = s[idx]

            # Option 1: Remove current parenthesis if quota remains
            if ch == "(" and rem_l > 0:
                if idx == 0 or s[idx - 1] != "(" or rem_l > 0:
                    dfs(idx + 1, balance, rem_l - 1, rem_r, path)
            elif ch == ")" and rem_r > 0:
                dfs(idx + 1, balance, rem_l, rem_r - 1, path)

            # Option 2: Keep current character
            path.append(ch)
            if ch == "(":
                dfs(idx + 1, balance + 1, rem_l, rem_r, path)
            elif ch == ")":
                dfs(idx + 1, balance - 1, rem_l, rem_r, path)
            else:
                # Lowercase English letter: always keep
                dfs(idx + 1, balance, rem_l, rem_r, path)
            path.pop()

        dfs(0, 0, remove_left, remove_right, [])
        return res