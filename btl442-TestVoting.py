


from io import StringIO
from unittest import main, TestCase

import Voting

class TestVoting (TestCase) :
    


    def test_ballot_class_1(self):
            b = Voting.Ballot([1, 2, 3])
            self.assertEqual(b.vote(),0)
            b.drop()
            self.assertEqual(b.marker,1)
            self.assertEqual(b.vote(),1)
        

    def test_ballot_class_2(self):
            b = Voting.Ballot([1, 2])
            self.assertEqual(len(b.votes), 2)
            self.assertEqual(b.vote(), 0)
            b.drop()
            self.assertEqual(b.marker, 1)

    def test_ballot_class_3(self):
            b = Voting.Ballot([1,2,3,4,5,6])
            self.assertEqual(len(b.votes),6)

    def test_ballot_class_4(self):
        b = Voting.Ballot([1,2,3,4])
        self.assertEqual(b.votes[0], 1)

    def test_ballot_class_5(self):
        b = Voting.Ballot([5,4,3,2,1])
        self.assertEqual(b.vote(), 4)

    def test_ballot_class_6(self):
        b = Voting.Ballot([5, 2,4])
        self.assertEqual(len(b.votes), 3)
        self.assertEqual(b.vote(), 4)
        b.drop()
        self.assertEqual(b.marker, 1)
        
        

    # -----
    # class candidate
    # -----

    def test_candidate_class_1(self):
        c = Voting.Candidate("a")
        self.assertEqual(c.name, "a")

    def test_candidate_class_2(self):
        c = Voting.Candidate("a")
        self.assertEqual(c.score, 0)

    def test_candidate_class_3(self):
        c = Voting.Candidate("a")
        self.assertEqual(c.still_in, True)

    def test_candidate_class_4(self):
        c = Voting.Candidate("a")
        c.add()
        self.assertEqual(c.score,1)
        c.flush()
        self.assertEqual(c.score,0)

    def test_candidate_class_5(self):
        c = Voting.Candidate("a")
        self.assertEqual(c.still_in, True)

    def test_candidate_class_6(self):
        c = Voting.Candidate("a")
        c.add()
        self.assertEqual(c.score,1)
        c.flush()
        self.assertEqual(c.score,0)
        

    

# ----
# main
# ----

main()
