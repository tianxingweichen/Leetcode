这道题采取桶排序的方法。
设置一个空桶数组，数组所有元素都为0,length = max(nums)+2，。给最大的整数后面留一位
将数列对应整数放置到空桶中。
此时空桶里一个未放置的位置就是Missing Positive。
注意将0位质1
