n=int(input())
s=[]
a=list(map(int,input().split()))
for i in range (n):
    s.insert(i,a[i])
print("Menor valor: %d" %(min(s)))
for i in range(n):
    if s[i]==min(s):
        pos=i
print("Posicao: %d" %pos)