class Solution:
    def backspaceCompare(self, S: str, T: str) :
        def mycode(a):
            while '#' in a:
                po=a.find('#')

                if po==0:
                    a=a.replace(a[po],'',1)
                else:
                    b=a[po-1]+'#'
                    a=a.replace(b,'')
            return a

        s=mycode(S)
        t=mycode(T)
        return s==t

