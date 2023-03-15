import sys
import random
num_reviewers = int(sys.argv[1])
num_teams = int(sys.argv[2])
coverage = int(sys.argv[3])

assignments = [set() for i in range(num_reviewers)]


for team_no in range(num_teams):
    randomized_reviewers = random.sample(range(num_reviewers), num_reviewers)
    min_num_reviews = min(len(a) for a in assignments)
    reviewers = set()
    i = 0
    while len(reviewers) < coverage:
        i = i % num_reviewers
        reviewer = randomized_reviewers[i]
        num_reviews_for_reviewer = len(assignments[reviewer])
        if num_reviews_for_reviewer == min_num_reviews:
            reviewers.add(reviewer)
            assignments[reviewer].add(team_no)
            min_num_reviews = min(len(a) for a in assignments)
        i += 1
    
    reviewers_csv = ",".join(str(r) for r in sorted(reviewers))
    print(f'team{team_no},{reviewers_csv}')

for i, a in enumerate(assignments):
    team_csv = ",".join(str(t) for t in sorted(a))
    print(f'judge{i},{team_csv}')
