class Solution:
    
    def isPalindrome(self, x):
        
        self.x = x
        
        x_str = str(x)
        x_rev = x_str[::-1]
        
        if x_str == x_rev:
            print('True')
        else:
            print('False')
    
p1 = Solution()
p1.isPalindrome(121)