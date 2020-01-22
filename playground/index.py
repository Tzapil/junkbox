seed = "[{seed}]".replace("{seed}", ','.join('"' + x + '"' for x in ["1","1","2","3"]))

print seed

import re

regex = re.compile(r'[abcd]+')

print str(regex)

old_arrr = [1,2,3,4]
cr_prfix = ["'" + str(x) + "'" for x in [1] + [1,2,3,4]]

print cr_prfix

# new_arr = [1].concat(old_arrr)

# print new_arr
# print [1].concat(old_arrr)
# print old_arrr