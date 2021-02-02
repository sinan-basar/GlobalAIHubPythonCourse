# Day2 - HomeWorks 1/2

n = 10

template_list = [ i**2 for i in range( -n, n, 1) ]

temporary_space = 0

print("Template list:",template_list)
print("Temporary space: ",temporary_space)

for i in range(n):
    temporary_space = template_list[i]
    template_list[i] = template_list[i+n]
    template_list[i+n] = temporary_space

print("Templat list:",template_list)
del temporary_space
