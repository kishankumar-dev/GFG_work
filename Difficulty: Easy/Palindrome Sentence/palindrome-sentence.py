class Solution:
	def isPalinSent(self, s):
		# code here  
		cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]