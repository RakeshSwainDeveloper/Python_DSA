def jweal_and_stoner(stones,jwel):
    s = set(jwel)
    count = 0
    for i in stones:
        if i in s:
            count += 1
    return count


def ransome_note(ransome_node,magagine):
    dic = {}
    for m in magagine:
        if m in dic:
            dic[m] += 1
        else:
            dic[m] = 1
    for r in ransome_node:
        # if r in dic:
        #     if dic[r] == 1:
        #         del dic[r]
        #     else:
        #         dic[r]-=1
        # else:
        #     return False
        if r not in dic:
            return False
        elif dic[r] == 1:
            del dic[r]
        else:
            dic[r] -= 1
    return True

def trap(height):
    max_height = 0
    min_height = 0
    i,trap_sum = max_height+1,0
    while max_height < len(height):
        for n in range(i,len(height)):
            if height[max_height] > height[i]:
                min_height = i
            else:
                if max_height != i:
                    pass

