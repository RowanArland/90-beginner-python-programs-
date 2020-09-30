team = ['teamA', 'teamB', 'teamC','teamD']
print("Original List: ",team)
team = [v for l in team
        for v in ('c', l)]
print("Original List: ",team)
