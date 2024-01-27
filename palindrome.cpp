#include<string>
using std::string;
class Solution {
public:
    bool isPalindrome(int x) 
    {
        int original_value = x;
     string given_value = to_string(x);
     string reversed_string;
     if(x < 0)
     {
         return false;
     }
     else
     {
         while(x != 0)
         {
             int temp = x%10;
             reversed_string += to_string(temp);
             x = x/10;
         }
     }
     if(given_value == reversed_string)
     {
         return true;
     }
     else if(original_value == 0)
     {
         return true;
     }
     else
     {
         return false;
     }
    }
};
