class Fibonacci():
   def __init__(self, a = 0, b = 1):
      self.a = a
      self.b = b

   def series(self):
      while(True):
         yield(self.b)
         self.a, self.b = self.b, self.a + self.b

f = Fibonacci()
for r in f.series():
   if r > 100: break
   print(r, end=" ")
