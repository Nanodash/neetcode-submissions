class Solution:

    WIDTH = 4  # fixed width for length field

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            length = len(s)
            # Format length as a fixed-width decimal, zero-padded
            parts.append(f"{length:0{self.WIDTH}d}{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i < n:
            # Read fixed-width length field
            length_str = s[i:i + self.WIDTH]
            length = int(length_str)
            i += self.WIDTH

            # Extract the string of that length
            res.append(s[i:i + length])
            i += length

        return res
