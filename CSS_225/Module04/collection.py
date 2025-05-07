# Author: Ishrak Rahman < admin@ishrak.xyz > 
# Last Edited: 5/6/2025
#
# Description:
# Prints out key and value from a dictionary using a loop
# 
# Objective:
# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print(author, "died in", date)
#    print "%s" % authors + " died in " + "%d." % Date
