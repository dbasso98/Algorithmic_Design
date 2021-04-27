# Homework Batch II: Trees and Algorithms

## Davide Basso - SM3500450

### Exercise 1

Let H be a Min-Heap containing n integer keys and let k be an integer
value. Solve the following exercises by using the procedures seen during
the course lessons:

(a) Write the pseudo-code of an in-place procedure RetrieveMax(H) to efficiently return the maximum value in H without deleting it and evaluate its complexity.

```RetrieveMax
def RetrieveMax(H):
    mid <- floor(H.size/2)
    max <- mid
    for i <- mid + 1 to H.size
        if max < H[i]
            max <- i
        endif
    endfor
    return max
enddef
```

In this algorithm we are dealing with a Min-Heap represented thorugh an array. We know from theory that in this way root node will be placed in $1^{st}$ position and each left and right child of $i-th$ node will be then respectively found $2i-th$ and $2i+1-th$ position.
Basically what we are doing is to exclude _a priori_ all the nodes that have children (and so that are $<=$ than other nodes due to the min-heap property) and then retrieve the maximum through a linear scan. The function returns the index of the maximum value.

In order to evaluate the complexity of this algorithm we just have to count the number of iterations performed by the for loop (all the operations inside it cost $\theta(1)$):
$$n - \lceil\frac{n}{2}\rceil \leq n$$
So we have that the algorithm belongs to $\theta(n)$.

(b) Write the pseudo-code of an in-place procedure DeleteMax(H) to efficiently delete the maximum value from H and evaluate its complexity.

``` DeleteMax
def DeleteMax(H):
    max <- RetrieveMax(H)
    swap(H, max, H.size)
    H.size <- H.size-1
    i <- max

    while not (is_root(i) or H[parent(i)] <= H[i]):
        swap(H, H[i], H[parent(i)])
        i <- parent(i)
    endwhile
enddef
```

Maximum value will be for sure a leaf node, so in order to remove it we can swap it with the last element of the heap and decrease by $1$ the heap size itself. 
However we need to be sure that the binary heap property is still satisfied. To do so we check if the parent is bigger than the newly changed child, if so we swap them and push the problem upwards until root is reached.

We can finally compute the overall complexity, which for sure will be strictly connected to _RetrieveMax(H)_ one, and in fact it's equal to:
$$\theta(n) + O(log(n))$$
where the second term is due to the bin-heap property checking (at most done $height(H) = log(n)$ times).

(c) Provide a working example for the worst case scenario of the procedure DeleteMax(H) on a heap H consisting in 8 nodes and simulate the execution of the function itself.

Let's take `H = [1,2,30,4,5,60,70,8]`. By applying the previously defined algorithm we find out that the maximum is placed in position $7$. Then the swap with the last element of the heap is operated. Now we have that `H = [1,2,30,4,5,60,8]` but bin-Heap property is no longer satisfied so the algorithm procedes with the swap between parent (30) and child node (8). Doing so the heap property is fixed and the final result is: `H = [1,2,8,4,5,60,30]`.

### Exercise 2

Let A be an array of n integer values (i.e., the values belong to $\Z$). Consider the problem of computing a vector B such that, for all $i \in [1; n], B[i]$ stores the number of elements smaller than $A[i]$ in $A[i + 1;\dots; n]$. More
formally:
$$ B[i] = |\{z\in[i + 1; n]: A[z] < A[i]\}| $$

(a) Evaluate the array B corresponding to `A=[2,-7,8,3,-5,-5,9,1,12,4]`.

The result is `B = [4,0,5,3,0,0,2,0,1,0]`.

(b) Write the pseudo-code of an algorithm belonging to $O(n^2)$ to solve the problem. Prove the asympotic complexity of the proposed solution and its correctness.

```smallerThan
def smallerThan(A):
    B <- array[A.size, default = 0]
    counter <- 0
    for i <- 1 to A.size:
        for j <- i+1 to A.size:
            if A[j] < A[i]:
                counter <- counter + 1
            endif
        endfor
        B[i] <- counter
        counter <- 0
    endfor

    return B
enddef
```
Using this kind of approach we are able to solve in 

(c) Assuming that there is only a constant number of values in A different from 0, write an efficient algorithm to solve the problem, evaluate its complexity and correctness.
