import collections

def groupAnagrams(strs):
    ans = collections.defaultdict(list) #default dict helps in avoiding keyerror.

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        #print("count is ",tuple(count))
        #print("ans ",ans)
        ans[tuple(count)].append(s)
    return ans.values()


def myfunc(strs):
        ana_dict={}
        final=[]
        flag={}
        for s in strs:
            count_dict={}
            flag[s]=0
            for i in range(len(s)):
                count_dict[s[i]]=1+count_dict.get(s[i],0)
                #print(count_dict)
            ana_dict[s]=count_dict
        #print(ana_dict[strs[0]])
        for i in range(len(strs)):
            temp_list=[]
            if(flag[strs[i]]==0):
                temp_list.append((strs[i]))
                flag[strs[i]]=1
                j=i+1
                while(j<len(strs)):
                    if( ana_dict[strs[i]]==ana_dict[strs[j]] and flag[strs[j]]==0 ):
                        temp_list.append(strs[j])
                        flag[strs[i]]=1
                        flag[strs[j]]=1
                        
                    #strs.remove[strs[j]]
                    #del ana_dict[strs[j]]
                    j+=1
                    #temp_list=json.dumps(temp_list)
                    #temp_list=str(temp_list)
                final.append((temp_list))
        return final
    


def main():
    strs=["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
    print(myfunc(strs))

    
if __name__=="__main__":
    main()
