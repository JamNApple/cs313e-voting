num_of_elections = 0
why = True
num_of_candidates = 0

class Ballot:

    def __init__(self, a = list):
        self.votes = a
        self.marker = 0
        

    def drop(self):
        #print("drop",self.votes, self.marker,"???")
        if self.marker < len(self.votes)-1:
            self.marker += 1

    def vote(self):
        print(self.votes[self.marker],self.votes, self.marker, "'''")
        return self.votes[self.marker]-1

class Candidate:

    def __init__ (self, a = str):
        self.name = a
        self.score = 0
        self.still_in = True

    def flush (self):
        self.score = 0
        print("flush")

    def add (self):
        self.score += 1
        print("add")


def voting_solve(readfile):

    file = open(readfile, 'r')
    num_of_elections = int(file.readline())
    file.readline()
    for v in range(num_of_elections):
        print(v)
        num_of_candidates = int(file.readline())
        candidate_list = []
        for v in range(num_of_candidates):
            candidate_list.append(Candidate(file.readline()))
            #print(candidate_list[v].name)
        #print(len(candidate_list))
        ballot_list = []
        key = True
        while key:            
            a=(file.readline())
            if a != "\n":
                b = []
                c = a.split()
                for v in c:
                    if v != " ":
                        b.append(int(v))
                ballot_list.append(Ballot(b))
               # print(b, len(b))
            if a == "\n":
                key = False
        find_winner(candidate_list, ballot_list)
        

def find_winner(candidate_list, ballot_list):

    while True:
        for candidate in candidate_list:
            candidate.flush()
        for ballot in ballot_list:            
            candidate_list[ballot.vote()].add()
        winners = []
        for v in range(len(candidate_list)):
            if candidate_list[v].score > len(ballot_list)/2:
                print(candidate_list[v].name)
                return candidate_list[v].name

            if check_for_tie(candidate_list) != []:

                for v in check_for_tie(candidate_list):
                    print(v.name, end = " ")
                print()    
                return check_for_tie(candidate_list)
        drop_marker(candidate_list,ballot_list)
        #print("lowest")
        
def drop_marker (can_list, bal_list):
    for v in can_list:
        if v.score !=0:
            lowest = v.score
    
    for v in can_list:
        if v.score == 0:
            v.still_in = False
        if v.score!= 0:
            v.still_in = True
        if v.score<lowest and v.still_in:
            lowest = v.score
        
    
    drop_list = []
    #print("low",lowest)
    for v in can_list:
        if v.score == lowest and v.still_in:
            drop_list.append(v)
            #print(v.name)
    to_drop = []
    for can in drop_list:
        for ballot in bal_list:
            if can_list[ballot.votes[ballot.marker]-1] == can:
                to_drop.append(ballot)
    for ballot in to_drop:
        ballot.drop()
    
    #print("dropmarker")
    
def check_for_tie(can_list):
    winners = []
    for v in can_list:
        if v.score !=0:
            lowest = v.score
    
    for v in can_list:
        if v.score == 0:
            v.still_in = False
        if v.score!= 0:
            v.still_in = True
        if v.score<lowest and v.still_in:
            lowest = v.score
        
    key = True
    for v in can_list:
        if v.still_in and v.score != lowest:
            key = False

    if key == True:
        #print("key is true")
        
        for v in can_list:
            if v.still_in:
                winners.append(v)
    #for v in winners:
        #print(v.name)
    
    return winners
    
    
voting_solve("tests5.txt")
