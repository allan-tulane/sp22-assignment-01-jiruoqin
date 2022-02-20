"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra+rb

    pass

def longest_run(mylist, key):
    ### TODO
    strikeMax = 0
    strikeCurr = 0
    for i in range(len(mylist)):
        if mylist[i] == key:
            strikeCurr += 1
        else:
            if strikeCurr > strikeMax:
                strikeMax = strikeCurr
            strikeCurr = 0
    if strikeCurr > strikeMax:
        strikeMax = strikeCurr
    return strikeMax


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
def longest_run_recursive(mylist, key):
    mylist = longest_run_recursive_part(mylist, key)
    return mylist.longest_size

def longest_run_recursive_part(mylist, key):
    ### TODO
    if (len(mylist) == 1):
        if mylist[0] == key:
            return Result(1,1,1,True)
        else:
            return Result(0,0,0,False)
    else:
        mid = len(mylist) // 2
        r1 = mylist[:mid]
        r2 = mylist[mid:]
        left = longest_run_recursive_part(r1, key)
        right = longest_run_recursive_part(r2, key)
        if left.is_entire_range and right.is_entire_range:
            temp = left.longest_size + right.longest_size
            return Result(temp,temp,temp,True)
        elif left.is_entire_range == False and right.is_entire_range:
            temp = left.right_size + right.longest_size
            return Result(left.left_size, temp, max(left.left_size,temp), False)
        elif right.is_entire_range == False and left.is_entire_range:
            temp = right.left_size + left.longest_size
            return Result(temp, right.right_size, max(right.right_size,temp), False)
        else:
            temp = right.left_size + left.right_size
            return Result(left.left_size, right.right_size, max(right.right_size,left.left_size,temp), False)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3

def test_foo():
  assert foo(0) == 0
  assert foo(1) == 1
  assert foo(2) == 1
  assert foo(3) == 2
  assert foo(4) == 3
  assert foo(5) == 5
  assert foo(6) == 8
  assert foo(7) == 13

def test_foo():
    assert foo(10) == 55

def test_foo2():
    assert foo(0) == 0
    assert foo(1) == 1

def test_longest_run_none():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 999) == 0

def test_longest_run():
	assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

def test_longest_run2():
	assert longest_run([12,12,12,8,12,12,0,12,1], 12) == 3
	assert longest_run([12,12,12,8,12,12,0,12,12,12,12], 12) ==4

def test_longest_run_hard():
    """
    This is a hard corner case that requires left_size and
    right_size to be calculated correctly when only one half 
    has is_entire_range==True.

    [6 12] [12 12] [12 6] [6 6]
    """
    assert to_value(longest_run([6, 12, 12, 12, 12, 6, 6, 6], 12)) == 4

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)

def test_longest_run_recursive_none():
    assert to_value(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 999)) == 0

def test_longest_run_recursive():
	assert to_value(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12)) == 3

def test_longest_run_recursive2():
	assert to_value(longest_run_recursive([12,12,12,8,12,12,0,12,1], 12)) == 3
	assert to_value(longest_run_recursive([12,12,12,8,12,12,0,12,12,12,12], 12)) == 4

def test_longest_run_recursive_hard():
    """
    This is a hard corner case that requires left_size and
    right_size to be calculated correctly when only one half 
    has is_entire_range==True.

    [6 12] [12 12] [12 6] [6 6]
    """
    assert to_value(longest_run_recursive([6, 12, 12, 12, 12, 6, 6, 6], 12)) == 4

test_longest_run2()