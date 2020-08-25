def merge(*args):
    arg_len = len(args)
    args = [iter(arg) for arg in args]
    idxs = [0] * arg_len
    mins = [next(arg) for arg in args]
    
    while len(args):
        min_ = min(mins)
        idx_ = mins.index(min_)
        
        try:
            idxs[idx_] += 1
            mins[idx_] = next(args[idx_])
        except StopIteration:
            del(args[idx_], idxs[idx_], mins[idx_])

        yield(min_)
