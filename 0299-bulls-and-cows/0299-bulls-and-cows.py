class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        s_cnt = [0] * 10
        g_cnt = [0] * 10

        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                s_digit = int(s_ch)
                g_digit = int(g_ch)

                if g_cnt[s_digit] > 0:
                    cows += 1
                    g_cnt[s_digit] -= 1
                else:
                    s_cnt[s_digit] += 1

                if s_cnt[g_digit] > 0:
                    cows += 1
                    s_cnt[g_digit] -= 1
                else:
                    g_cnt[g_digit] += 1

        return f"{bulls}A{cows}B"