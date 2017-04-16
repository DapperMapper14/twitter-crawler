import json

def filterHashtag(in_json, out_json, keyword)
    # Load in empty data file to store clean data
    with open(out_json, "w") as json_outfile:
        # Load in original march madness file and loop over records
        with open(in_json) as tFile:
            for t in tFile:
                try:
                    tweet = json.loads(t)
                    for ht in tweet["entities"]["hashtags"]:
                        match = ht["text"]
                        if match.lower() == keyword.lower():
                            json.dump(tweet, json_outfile)
                            json_outfile.write('\n')
                        else:
                            continue
                except: 
                    continue
    print "Added all entries that matched keyword: {0}".format(keyword)
    return None

def removeDuplicates(in_json, out_json, unique_id)
    with open("march-madness-final.json", "w") as nf:
        # Load in original march madness file and loop over records
        with open("march-madness-combo.json") as f:
            uniques = []
            for t in f:
                tweet = json.loads(t)
                if tweet[unique_id] in uniques:
                    continue
                else:
                    uniques.append(tweet[unique_id])
                    json.dump(tweet, nf)
                    nf.write('\n')
    print "Removed all duplicates containing the same {0}".format(unique_id)
    return None
            
print "Complete"

def joinJSON (jsonFile1, jsonFile2, outFile):
    # load json objects to dictionaries
    with open(jsonFile1) as f1:
        json1 = map(json.loads, f1)
    with open(jsonFile2) as f2:
        json2 = map(json.loads, f2)
    
    joined = json1+json2

    with open(outFile, "w") as nf:
        for j in joined:
            json.dump(j, nf)
            nf.write('\n')
    print "Joined JSON file written to {0}".format(outFile)
    return None
