def sum_of_all_subarray_sums(A):
    N=len(A)
    total=0

    for i in range(N):
        total+=(N-i)*(i+1)*A[i]

    return total

A=list(map(int,input().split()))
result=sum_of_all_subarray_sums(A)
print(result)

