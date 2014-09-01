def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").
  siteUserMap = dict()
  for s in site_list:
    if not s in siteUserMap:
      siteUserMap[s] = set()
  for i in range(len(site_list)):
      siteUserMap[site_list[i]].add(user_list[i])
  affinityPair = ("this", "that")
  tempMax = -1
 
  listOfSites = siteUserMap.keys()
  for i in range(len(listOfSites)):
    for j in range(i+1, len(listOfSites)):
         count = 0
         for user in siteUserMap[listOfSites[i]]:
           if user in siteUserMap[listOfSites[j]]:
             count += 1
         if count > tempMax:
           tempMax = count
           affinityPair = (listOfSites[i], listOfSites[j])
  if(affinityPair[0] > affinityPair[1]):
    affinityPair = (affinityPair[1], affinityPair[0])
  return affinityPair
